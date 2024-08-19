import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class StateUpdater {
    private static final Map<String, Double> energyConsumptionMap = new HashMap<>();
    private static final Map<Integer, Double> hydroPowerMap = new HashMap<>();
    private static final double ENERGY_PER_100K_POPULATION = 0.012;

    private static final double SUBSTATION_BIG_CAPACITY = 0.75;
    private static final double SUBSTATION_CAPACITY = 0.10;

    static {
        energyConsumptionMap.put("arms_factory", 0.075);
        energyConsumptionMap.put("industrial_complex", 0.075);
        energyConsumptionMap.put("ammunition_plant", 0.075);
        energyConsumptionMap.put("dockyard", 0.1);
        energyConsumptionMap.put("synthetic_refinery", 0.05);
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

    public boolean processStateFile(Path stateFile, boolean addSubstations) throws IOException {
        System.out.println("File processing: " + stateFile.getFileName());
        List<String> lines = Files.readAllLines(stateFile);
        boolean modified = false;

        int stateId = extractStateId(lines);
        if (stateId == -1) {
            System.out.println("State ID not found in the file: " + stateFile.getFileName());
            return false;
        }

        int historyIndex = findHistoryIndex(lines);
        int buildingsIndex = findBuildingsIndex(lines, historyIndex);

        if (buildingsIndex == -1) {
            if (historyIndex != -1) {
                lines.add(historyIndex + 1, "\tbuildings = {\n\t}");
                System.out.println("Created section buildings = {} in the file: " + stateFile.getFileName());
                buildingsIndex = historyIndex + 1;
                modified = true;
            } else {
                System.out.println("History = {} section not found in the file: " + stateFile.getFileName());
                return false;
            }
        }

        if (addSubstations) {
            double totalEnergyConsumption = calculateTotalEnergyConsumption(lines);
            int manpower = extractManpower(lines);

            totalEnergyConsumption += (manpower / 100000.0) * ENERGY_PER_100K_POPULATION;

            // Добавление мощности ГЭC
            if (hydroPowerMap.containsKey(stateId)) {
                double hydroPower = hydroPowerMap.get(stateId);
                totalEnergyConsumption += hydroPower;
                System.out.println("Added hpp for state " + stateId + ": " + hydroPower + " GW");
            }

            System.out.println("Total energy consumption: " + totalEnergyConsumption + " GW");

            int bigSubstations = (int) Math.ceil(totalEnergyConsumption / SUBSTATION_BIG_CAPACITY);
            int smallSubstations = (int) Math.ceil((totalEnergyConsumption % SUBSTATION_BIG_CAPACITY) / SUBSTATION_CAPACITY);

            System.out.println("Required number of electrical_substation_big: " + bigSubstations);
            System.out.println("Required number of electrical_substation: " + smallSubstations);

            modified = updateSubstations(lines, bigSubstations, smallSubstations, buildingsIndex);
        } else {
            modified = removeSubstations(lines, buildingsIndex);
        }

        if (modified) {
            Files.write(stateFile, lines);
            System.out.println("File updated: " + stateFile.getFileName());
        } else {
            System.out.println("No changes are required for the file: " + stateFile.getFileName());
        }

        return modified;
    }

    private double calculateTotalEnergyConsumption(List<String> lines) {
        double totalEnergyConsumption = 0.0;
        Pattern buildingsPattern = Pattern.compile("\\s*(\\w+)\\s*=\\s*(\\d+)");

        for (String line : lines) {
            Matcher buildingsMatcher = buildingsPattern.matcher(line);
            if (buildingsMatcher.find()) {
                String buildingType = buildingsMatcher.group(1);
                int count = Integer.parseInt(buildingsMatcher.group(2));
                double energyConsumption = energyConsumptionMap.getOrDefault(buildingType, 0.0) * count;
                totalEnergyConsumption += energyConsumption;

                if (energyConsumption > 0) {
                    System.out.println("Building type: " + buildingType + ", amount: " + count + ", energy consumption: " + energyConsumption + " GW");
                }
            }
        }
        return totalEnergyConsumption;
    }

    private int extractStateId(List<String> lines) {
        Pattern idPattern = Pattern.compile("id\\s*=\\s*(\\d+)");
        for (String line : lines) {
            Matcher idMatcher = idPattern.matcher(line);
            if (idMatcher.find()) {
                return Integer.parseInt(idMatcher.group(1));
            }
        }
        return -1;
    }

    private int extractManpower(List<String> lines) {
        int manpower = 0;
        Pattern manpowerPattern = Pattern.compile("manpower\\s*=\\s*(\\d+)");
        for (String line : lines) {
            Matcher manpowerMatcher = manpowerPattern.matcher(line);
            if (manpowerMatcher.find()) {
                manpower = Integer.parseInt(manpowerMatcher.group(1));
                System.out.println("State population: " + manpower);
                break;
            }
        }
        return manpower;
    }

    private boolean updateSubstations(List<String> lines, int bigSubstations, int smallSubstations, int buildingsIndex) {
        boolean modified = false;
        String indentation = getIndentation(lines.get(buildingsIndex + 1));
        boolean foundBigSubstation = false;
        boolean foundSmallSubstation = false;

        for (int i = buildingsIndex + 1; i < lines.size(); i++) {
            String line = lines.get(i).trim();
            if (line.startsWith("electrical_substation_big")) {
                if (bigSubstations > 0) {
                    lines.set(i, indentation + "electrical_substation_big = " + bigSubstations);
                    System.out.println("Updated the number of electrical_substation_big: " + bigSubstations);
                    modified = true;
                } else {
                    lines.remove(i);
                    System.out.println("electrical_substation_big removed");
                    i--;
                }
                foundBigSubstation = true;
            } else if (line.startsWith("electrical_substation")) {
                if (smallSubstations > 0) {
                    lines.set(i, indentation + "electrical_substation = " + smallSubstations);
                    System.out.println("Updated the number of electrical_substation: " + smallSubstations);
                    modified = true;
                } else {
                    lines.remove(i);
                    System.out.println("electrical_substation removed");
                    i--;
                }
                foundSmallSubstation = true;
            } else if (line.startsWith("}")) {
                break;
            }
        }

        if (!foundBigSubstation && bigSubstations > 0) {
            lines.add(buildingsIndex + 1, indentation + "electrical_substation_big = " + bigSubstations);
            System.out.println("electrical_substation_big added: " + bigSubstations);
            modified = true;
        }
        if (!foundSmallSubstation && smallSubstations > 0) {
            lines.add(buildingsIndex + 1, indentation + "electrical_substation = " + smallSubstations);
            System.out.println("electrical_substation added: " + smallSubstations);
            modified = true;
        }

        return modified;
    }

    private boolean removeSubstations(List<String> lines, int buildingsIndex) {
        boolean modified = false;

        for (int i = buildingsIndex + 1; i < lines.size(); i++) {
            String line = lines.get(i).trim();
            if (line.startsWith("electrical_substation_big") || line.startsWith("electrical_substation")) {
                System.out.println("Substation has been removed: " + line);
                lines.remove(i);
                i--;
                modified = true;
            } else if (line.startsWith("}")) {
                break;
            }
        }

        return modified;
    }

    private int findHistoryIndex(List<String> lines) {
        for (int i = 0; i < lines.size(); i++) {
            if (lines.get(i).trim().startsWith("history = {")) {
                return i;
            }
        }
        return -1;
    }

    private int findBuildingsIndex(List<String> lines, int historyIndex) {
        if (historyIndex == -1) return -1;

        for (int i = historyIndex + 1; i < lines.size(); i++) {
            if (lines.get(i).trim().startsWith("buildings = {")) {
                return i;
            }
        }
        return -1;
    }

    private String getIndentation(String line) {
        int index = 0;
        while (index < line.length() && Character.isWhitespace(line.charAt(index))) {
            index++;
        }
        return line.substring(0, index);
    }
}