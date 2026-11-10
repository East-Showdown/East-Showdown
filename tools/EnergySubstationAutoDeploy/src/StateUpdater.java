import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.charset.CharacterCodingException;
import java.nio.charset.Charset;
import java.nio.charset.CodingErrorAction;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class StateUpdater {
    private static final Map<String, Double> energyConsumptionMap = new HashMap<>();
    private static final Map<Integer, Double> hydroPowerMap = new HashMap<>();
    private static final double ENERGY_PER_100K_POPULATION = 0.012;

    private static final double SUBSTATION_BIG_CAPACITY = 0.8;
    private static final double SUBSTATION_CAPACITY = 0.13;
    private static final double EPS = 1e-9;

    private static final String BIG = "electrical_substation_big";
    private static final String SMALL = "electrical_substation";

    // key = number, not preceded by a word char or '.' (so dates like 1939.1.1 are not matched)
    private static final Pattern ENTRY_PATTERN = Pattern.compile("(?<![\\w.])(\\w+)\\s*=\\s*(\\d+)(?![\\w.])");
    private static final Pattern SUBSTATION_PATTERN =
            Pattern.compile("(?<![\\w.])(" + BIG + "|" + SMALL + ")\\s*=\\s*(\\d+)(?![\\w.])");

    static {
        energyConsumptionMap.put("arms_factory", 0.075);
        energyConsumptionMap.put("industrial_complex", 0.075);
        energyConsumptionMap.put("ammunition_plant", 0.075);
        energyConsumptionMap.put("dockyard", 0.1);
        energyConsumptionMap.put("synthetic_refinery", 0.05);
        energyConsumptionMap.put("electronic_factory", 0.1);
        energyConsumptionMap.put("nuclear_power_plant", 1.0);
        energyConsumptionMap.put("thermal_power_plant", 0.2);
        energyConsumptionMap.put("solar_power_plant", 0.01);
        energyConsumptionMap.put("wind_power_plant", 0.02);

        //Хардкод мощностей ГЭС
        hydroPowerMap.put(644, 0.336);
        hydroPowerMap.put(671, 0.35);
        hydroPowerMap.put(208, 0.7);
        hydroPowerMap.put(169, 0.3);
        hydroPowerMap.put(158, 0.5);
        hydroPowerMap.put(73, 0.5);
        hydroPowerMap.put(74, 2.8);
        hydroPowerMap.put(515, 1.5);
        hydroPowerMap.put(42, 2.5);
        hydroPowerMap.put(17, 1.4);
        hydroPowerMap.put(16, 0.6);
        hydroPowerMap.put(444, 0.21);
        hydroPowerMap.put(21, 0.1);
        hydroPowerMap.put(32, 0.8);
        hydroPowerMap.put(85, 0.2);
        hydroPowerMap.put(97, 0.5);
        hydroPowerMap.put(134, 0.2);
        hydroPowerMap.put(347, 2.4);
        hydroPowerMap.put(328, 1.2);
    }

    /** Parsed view of a state file: comments and quoted strings blanked out, brace depth per char. */
    private static final class Parsed {
        final String text;
        final String analysis;
        final int[] depth; // depth before each char

        Parsed(String text) {
            this.text = text;
            char[] a = text.toCharArray();
            boolean inQuote = false, inComment = false;
            for (int i = 0; i < a.length; i++) {
                char c = a[i];
                if (c == '\n') {
                    inComment = false;
                    inQuote = false;
                    continue;
                }
                if (inComment) {
                    a[i] = ' ';
                } else if (inQuote) {
                    if (c == '"') inQuote = false;
                    a[i] = ' ';
                } else if (c == '#') {
                    inComment = true;
                    a[i] = ' ';
                } else if (c == '"') {
                    inQuote = true;
                    a[i] = ' ';
                }
            }
            this.analysis = new String(a);
            this.depth = new int[a.length + 1];
            int d = 0;
            for (int i = 0; i < a.length; i++) {
                depth[i] = d;
                if (a[i] == '{') d++;
                else if (a[i] == '}') d--;
            }
            depth[a.length] = d;
        }

        /** Returns {openBraceIndex, closeBraceIndex} of "key = {" found at the given depth in [from, to), or null. */
        int[] findBlock(String key, int requiredDepth, int from, int to) {
            Matcher m = Pattern.compile("(?<![\\w.])" + Pattern.quote(key) + "\\s*=\\s*\\{").matcher(analysis);
            m.region(from, to);
            while (m.find()) {
                if (depth[m.start()] == requiredDepth) {
                    int open = m.end() - 1;
                    int close = matchingClose(open);
                    if (close != -1) return new int[]{open, close};
                }
            }
            return null;
        }

        int matchingClose(int open) {
            int target = depth[open];
            for (int i = open + 1; i < analysis.length(); i++) {
                if (analysis.charAt(i) == '}' && depth[i] == target + 1) return i;
            }
            return -1;
        }

        /** Matches of the pattern in (open, close) that sit directly inside that block (not in sub-blocks). */
        List<Matcher> directMatches(Pattern p, int open, int close) {
            List<Matcher> result = new ArrayList<>();
            int inner = depth[open] + 1;
            Matcher m = p.matcher(analysis);
            m.region(open + 1, close);
            while (m.find()) {
                if (depth[m.start()] == inner && depth[m.end() - 1] == inner) {
                    Matcher copy = p.matcher(analysis);
                    copy.region(m.start(), m.end());
                    copy.lookingAt();
                    result.add(copy);
                }
            }
            return result;
        }

        int lineStart(int idx) {
            return text.lastIndexOf('\n', idx - 1) + 1;
        }

        String indentOfLine(int idx) {
            int s = lineStart(idx);
            int e = s;
            while (e < text.length() && (text.charAt(e) == ' ' || text.charAt(e) == '\t')) e++;
            return text.substring(s, e);
        }
    }

    public boolean processStateFile(Path stateFile, boolean addSubstations) throws IOException {
        String name = stateFile.getFileName().toString();
        System.out.println("File processing: " + name);

        byte[] bytes = Files.readAllBytes(stateFile);
        boolean bom = bytes.length >= 3 && (bytes[0] & 0xFF) == 0xEF && (bytes[1] & 0xFF) == 0xBB && (bytes[2] & 0xFF) == 0xBF;
        int offset = bom ? 3 : 0;
        Charset charset = StandardCharsets.UTF_8;
        String raw;
        try {
            raw = StandardCharsets.UTF_8.newDecoder()
                    .onMalformedInput(CodingErrorAction.REPORT)
                    .onUnmappableCharacter(CodingErrorAction.REPORT)
                    .decode(ByteBuffer.wrap(bytes, offset, bytes.length - offset))
                    .toString();
        } catch (CharacterCodingException e) {
            // Not UTF-8: read byte-for-byte so the file is written back unchanged except for our edits
            charset = StandardCharsets.ISO_8859_1;
            raw = new String(bytes, offset, bytes.length - offset, charset);
        }
        boolean crlf = raw.contains("\r\n");
        String original = raw.replace("\r\n", "\n");
        String text = original;

        Parsed p = new Parsed(text);
        int[] state = p.findBlock("state", 0, 0, p.analysis.length());
        if (state == null) {
            System.out.println("state = { } block not found in the file: " + name);
            return false;
        }

        int stateId = findDirectNumber(p, "id", state);
        if (stateId == -1) {
            System.out.println("State ID not found in the file: " + name);
            return false;
        }

        int[] history = p.findBlock("history", 1, state[0] + 1, state[1]);
        if (history == null) {
            System.out.println("History = {} section not found in the file: " + name);
            return false;
        }

        int[] buildings = p.findBlock("buildings", 2, history[0] + 1, history[1]);
        if (buildings == null) {
            if (!addSubstations) {
                System.out.println("No changes are required for the file: " + name);
                return false;
            }
            String indent = p.indentOfLine(history[0]) + "\t";
            String block = "\n" + indent + "buildings = {\n" + indent + "}";
            text = text.substring(0, history[0] + 1) + block + text.substring(history[0] + 1);
            System.out.println("Created section buildings = {} in the file: " + name);
            p = new Parsed(text);
            state = p.findBlock("state", 0, 0, p.analysis.length());
            history = p.findBlock("history", 1, state[0] + 1, state[1]);
            buildings = p.findBlock("buildings", 2, history[0] + 1, history[1]);
        }

        // Indentation for entries inside buildings: use an existing entry's indent if it is on its own line
        String entryIndent = p.indentOfLine(buildings[0]) + "\t";
        List<Matcher> entries = p.directMatches(ENTRY_PATTERN, buildings[0], buildings[1]);
        for (Matcher m : entries) {
            int ls = p.lineStart(m.start());
            if (ls > buildings[0] && p.text.substring(ls, m.start()).trim().isEmpty()) {
                entryIndent = p.text.substring(ls, m.start());
                break;
            }
        }

        int big = 0, small = 0;
        if (addSubstations) {
            double total = 0.0;
            for (Matcher m : entries) {
                String type = m.group(1);
                int count = Integer.parseInt(m.group(2));
                double consumption = energyConsumptionMap.getOrDefault(type, 0.0) * count;
                if (consumption > 0) {
                    System.out.println("Building type: " + type + ", amount: " + count + ", energy consumption: " + round(consumption) + " GW");
                    total += consumption;
                }
            }

            int manpower = Math.max(0, findDirectNumber(p, "manpower", state));
            System.out.println("State population: " + manpower);
            total += (manpower / 100000.0) * ENERGY_PER_100K_POPULATION;

            // Добавление мощности ГЭC
            if (hydroPowerMap.containsKey(stateId)) {
                double hydroPower = hydroPowerMap.get(stateId);
                total += hydroPower;
                System.out.println("Added hpp for state " + stateId + ": " + hydroPower + " GW");
            }

            System.out.println("Total energy consumption: " + round(total) + " GW");

            // Big substations cover whole 0.75 GW chunks, small ones cover the remainder.
            big = (int) Math.floor(total / SUBSTATION_BIG_CAPACITY + EPS);
            double remainder = total - big * SUBSTATION_BIG_CAPACITY;
            small = remainder > EPS ? (int) Math.ceil(remainder / SUBSTATION_CAPACITY - EPS) : 0;
            // If the remainder needs more small capacity than one big substation provides, use a big one instead.
            if (small * SUBSTATION_CAPACITY >= SUBSTATION_BIG_CAPACITY - EPS) {
                big++;
                small = 0;
            }

            System.out.println("Required number of " + BIG + ": " + big);
            System.out.println("Required number of " + SMALL + ": " + small);
        }

        // Existing substation entries directly in the buildings block.
        // Keep the first entry of each type and change only its number, so the rest of the line
        // (indentation, trailing spaces, comments) stays byte-for-byte the same.
        List<Matcher> existing = p.directMatches(SUBSTATION_PATTERN, buildings[0], buildings[1]);
        List<int[]> deletions = new ArrayList<>();   // {start, end}
        List<int[]> numberEdits = new ArrayList<>(); // {start, end, newValue}
        boolean haveBig = false, haveSmall = false;
        for (Matcher m : existing) {
            boolean isBig = m.group(1).equals(BIG);
            int wanted = addSubstations ? (isBig ? big : small) : 0;
            boolean seen = isBig ? haveBig : haveSmall;
            if (wanted > 0 && !seen) {
                if (Integer.parseInt(m.group(2)) != wanted) {
                    numberEdits.add(new int[]{m.start(2), m.end(2), wanted});
                    System.out.println("Updated the number of " + m.group(1) + ": " + m.group(2) + " -> " + wanted);
                }
            } else {
                deletions.add(new int[]{m.start(), m.end()});
                System.out.println("Substation has been removed: " + p.text.substring(m.start(), m.end()));
            }
            if (isBig) haveBig = true; else haveSmall = true;
        }

        // Apply edits from the end of the file backwards so earlier offsets stay valid
        List<int[]> all = new ArrayList<>();
        for (int[] d : deletions) all.add(new int[]{d[0], d[1], -1});
        all.addAll(numberEdits);
        all.sort((a, b) -> Integer.compare(b[0], a[0]));
        StringBuilder sb = new StringBuilder(text);
        for (int[] edit : all) {
            int s = edit[0], e = edit[1];
            if (edit[2] >= 0) {
                sb.replace(s, e, String.valueOf(edit[2]));
                continue;
            }
            int ls = sb.lastIndexOf("\n", s - 1) + 1;
            int le = sb.indexOf("\n", e);
            if (le == -1) le = sb.length();
            String before = sb.substring(ls, s), after = sb.substring(e, le);
            if (before.trim().isEmpty() && after.trim().isEmpty() && ls > 0) {
                sb.delete(ls - 1, le); // whole line, including the preceding newline
            } else {
                // Shared line: drop the entry and the whitespace right before it
                while (s > ls && (sb.charAt(s - 1) == ' ' || sb.charAt(s - 1) == '\t')) s--;
                sb.delete(s, e);
            }
        }
        text = sb.toString();

        int insertBig = (addSubstations && !haveBig) ? big : 0;
        int insertSmall = (addSubstations && !haveSmall) ? small : 0;
        if (insertBig > 0 || insertSmall > 0) {
            p = new Parsed(text);
            state = p.findBlock("state", 0, 0, p.analysis.length());
            history = p.findBlock("history", 1, state[0] + 1, state[1]);
            buildings = p.findBlock("buildings", 2, history[0] + 1, history[1]);
            int insertAt = buildings[0] + 1;

            StringBuilder ins = new StringBuilder();
            if (insertBig > 0) {
                ins.append("\n").append(entryIndent).append(BIG).append(" = ").append(insertBig);
                System.out.println(BIG + " added: " + insertBig);
            }
            if (insertSmall > 0) {
                ins.append("\n").append(entryIndent).append(SMALL).append(" = ").append(insertSmall);
                System.out.println(SMALL + " added: " + insertSmall);
            }

            // If something else follows "{" on the same line, move it to its own line
            int le = text.indexOf('\n', insertAt);
            if (le == -1) le = text.length();
            String restOfLine = p.analysis.substring(insertAt, le);
            if (!restOfLine.trim().isEmpty()) {
                int k = insertAt;
                while (k < text.length() && (text.charAt(k) == ' ' || text.charAt(k) == '\t')) k++;
                String rest = text.substring(k);
                boolean closesHere = rest.startsWith("}");
                ins.append("\n").append(closesHere ? p.indentOfLine(buildings[0]) : entryIndent);
                text = text.substring(0, insertAt) + ins + rest;
            } else {
                text = text.substring(0, insertAt) + ins + text.substring(insertAt);
            }
        }

        if (text.equals(original)) {
            System.out.println("No changes are required for the file: " + name);
            return false;
        }

        String out = crlf ? text.replace("\n", "\r\n") : text;
        byte[] body = out.getBytes(charset);
        byte[] result;
        if (bom) {
            result = new byte[body.length + 3];
            result[0] = (byte) 0xEF;
            result[1] = (byte) 0xBB;
            result[2] = (byte) 0xBF;
            System.arraycopy(body, 0, result, 3, body.length);
        } else {
            result = body;
        }
        Files.write(stateFile, result);
        System.out.println("File updated: " + name);
        return true;
    }

    /** First "key = number" directly inside the given block, or -1. */
    private int findDirectNumber(Parsed p, String key, int[] block) {
        Pattern pattern = Pattern.compile("(?<![\\w.])" + Pattern.quote(key) + "\\s*=\\s*(\\d+)(?![\\w.])");
        List<Matcher> matches = p.directMatches(pattern, block[0], block[1]);
        return matches.isEmpty() ? -1 : Integer.parseInt(matches.get(0).group(1));
    }

    private static String round(double v) {
        return String.valueOf(Math.round(v * 1000.0) / 1000.0);
    }
}
