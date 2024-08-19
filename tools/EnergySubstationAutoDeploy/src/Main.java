import java.io.File;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StateUpdater stateUpdater = new StateUpdater();

        System.out.print("Enter the path to the history/states: ");
        String path = scanner.nextLine();
        File folder = new File(path);

        if (!folder.exists() || !folder.isDirectory()) {
            System.out.println("Invalid path or directory not found.");
            return;
        }

        while (true) {
            System.out.println("Select action:");
            System.out.println("1: Deploy substations");
            System.out.println("2: Delete electrical_substation_big; electrical_substation substations");
            System.out.println("3: Exit");
            int input = scanner.nextInt();

            switch (input) {
                case 1:
                    processFiles(folder, stateUpdater, true);
                    break;
                case 2:
                    processFiles(folder, stateUpdater, false);
                    break;
                case 3:
                    System.out.println("Termination of the program.");
                    return;
                default:
                    System.out.println("Try again.");
            }
        }
    }

    private static void processFiles(File folder, StateUpdater stateUpdater, boolean addSubstations) {
        File[] files = folder.listFiles((dir, name) -> name.endsWith(".txt"));

        if (files == null || files.length == 0) {
            System.out.println("No files to process.");
            return;
        }

        int totalFiles = files.length;
        int filesUpdated = 0;

        for (File file : files) {
            try {
                if (stateUpdater.processStateFile(file.toPath(), addSubstations)) {
                    filesUpdated++;
                }
            } catch (Exception e) {
                System.out.println("Error during file processing " + file.getName() + ": " + e.getMessage());
            }
        }

        System.out.println("Files processed: " + filesUpdated + "/" + totalFiles);
    }
}
