import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    //Даже после "успешной отработки" программы требуется частично ручками поработать
    private static final double ENERGY_PER_ARMS_FACTORY = 0.075;
    private static final double ENERGY_PER_INDUSTRIAL_COMPLEX = 0.075;
    private static final double ENERGY_PER_AMMUNITION_PLANT = 0.075;
    private static final double ENERGY_PER_DOCKYARD = 0.1;
    private static final double ENERGY_PER_SYNTHETIC_REFINERY = 0.05;
    private static final double ENERGY_PER_100K_POPULATION = 0.012;

    private static final double SUBSTATION_BIG_CAPACITY = 0.75;
    private static final double SUBSTATION_CAPACITY = 0.10;

    public static void main(String[] args) {
        File folder = new File("C:/Users/ksyx7/Documents/GitHub/East-Showdown/history/states"); //офк, тут должен быть ваш путь
        File[] stateFiles = folder.listFiles((dir, name) -> name.endsWith(".txt"));

        int totalFiles = 0;
        int modifiedFiles = 0;

        if (stateFiles != null) {
            totalFiles = stateFiles.length;
            for (File stateFile : stateFiles) {
                try {
                    if (processStateFile(stateFile.toPath())) {
                        modifiedFiles++;
                        System.out.println("File modified: " + stateFile.getName());
                    } else {
                        System.out.println("File not modified: " + stateFile.getName());
                    }
                } catch (IOException e) {
                    System.err.println("Error processing file: " + stateFile.getName());
                    e.printStackTrace();
                }
            }
        }

        System.out.println("Total files processed: " + totalFiles);
        System.out.println("Files modified: " + modifiedFiles);
    }

    private static boolean processStateFile(Path stateFile) throws IOException {
        List<String> lines = Files.readAllLines(stateFile);
        double totalEnergyConsumption = 0.0;
        int manpower = 0;
        boolean hasBigSubstation = false;
        boolean hasSmallSubstation = false;
        boolean modified = false;

        Pattern manpowerPattern = Pattern.compile("manpower\\s*=\\s*(\\d+)");
        Pattern buildingsPattern = Pattern.compile("(arms_factory|industrial_complex|ammunition_plant|dockyard|synthetic_refinery)\\s*=\\s*(\\d+)");
        Pattern substationBigPattern = Pattern.compile("\\s*electrical_substation_big\\s*=\\s*(\\d+)");
        Pattern substationPattern = Pattern.compile("\\s*electrical_substation\\s*=\\s*(\\d+)");

        for (String line : lines) {
            Matcher manpowerMatcher = manpowerPattern.matcher(line);
            if (manpowerMatcher.find()) {
                manpower = Integer.parseInt(manpowerMatcher.group(1));
            }

            Matcher buildingsMatcher = buildingsPattern.matcher(line);
            if (buildingsMatcher.find()) {
                String buildingType = buildingsMatcher.group(1);
                int count = Integer.parseInt(buildingsMatcher.group(2));
                totalEnergyConsumption += calculateEnergyConsumption(buildingType, count);
            }

            Matcher substationBigMatcher = substationBigPattern.matcher(line);
            if (substationBigMatcher.find()) {
                hasBigSubstation = true;
            }

            Matcher substationMatcher = substationPattern.matcher(line);
            if (substationMatcher.find()) {
                hasSmallSubstation = true;
            }
        }

        totalEnergyConsumption += (manpower / 100000.0) * ENERGY_PER_100K_POPULATION;

        int bigSubstations = (int) (totalEnergyConsumption / SUBSTATION_BIG_CAPACITY);
        double remainingEnergy = totalEnergyConsumption % SUBSTATION_BIG_CAPACITY;
        int smallSubstations = (int) Math.ceil(remainingEnergy / SUBSTATION_CAPACITY);

        System.out.println("File: " + stateFile.getFileName());
        System.out.println("Total Energy Consumption: " + totalEnergyConsumption);
        System.out.println("Big Substations needed: " + bigSubstations + ", Small Substations needed: " + smallSubstations);
        System.out.println("Big Substations present: " + hasBigSubstation + ", Small Substations present: " + hasSmallSubstation);

        if (bigSubstations == 0 && smallSubstations == 0 && totalEnergyConsumption > 0) {
            smallSubstations = 1;
        }

        if ((!hasBigSubstation && bigSubstations > 0) || (!hasSmallSubstation && smallSubstations > 0)) {
            addSubstations(lines, bigSubstations, smallSubstations);
            Files.write(stateFile, lines);
            modified = true;
        } else {
            System.out.println("File: " + stateFile.getFileName() + " has too low energy consumption.");
        }

        return modified;
    }

    private static double calculateEnergyConsumption(String buildingType, int count) {
        switch (buildingType) {
            case "arms_factory":
                return count * ENERGY_PER_ARMS_FACTORY;
            case "industrial_complex":
                return count * ENERGY_PER_INDUSTRIAL_COMPLEX;
            case "ammunition_plant":
                return count * ENERGY_PER_AMMUNITION_PLANT;
            case "dockyard":
                return count * ENERGY_PER_DOCKYARD;
            case "synthetic_refinery":
                return count * ENERGY_PER_SYNTHETIC_REFINERY;
            default:
                return 0;
        }
    }

    private static void addSubstations(List<String> lines, int bigSubstations, int smallSubstations) {
        int buildingsIndex = findBuildingsIndex(lines);
        if (buildingsIndex != -1) {
            String indentation = getIndentation(lines.get(buildingsIndex + 1));

            if (bigSubstations > 0) {
                lines.add(buildingsIndex + 1, indentation + "electrical_substation_big = " + bigSubstations);
            }
            if (smallSubstations > 0) {
                lines.add(buildingsIndex + 1, indentation + "electrical_substation = " + smallSubstations);
            }
        }
    }

    private static int findBuildingsIndex(List<String> lines) {
        for (int i = 0; i < lines.size(); i++) {
            if (lines.get(i).trim().startsWith("buildings = {")) {
                return i;
            }
        }
        return -1;
    }

    private static String getIndentation(String line) {
        int index = 0;
        while (index < line.length() && Character.isWhitespace(line.charAt(index))) {
            index++;
        }
        return line.substring(0, index);
    }
}
