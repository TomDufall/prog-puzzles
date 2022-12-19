import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class RopeSimulationImproved {
    int[][] knots = new int[10][2];

    HashSet<String> history = new HashSet<String>();

    public void printKnots() {
        String[] points = new String[10];
        for (int i = 0; i < 10; i++) {
            points[i] = Arrays.toString(knots[i]);
        }
        System.out.println(Arrays.toString(points));
    }

    // add history support
    private void applyKnotStep(int index) {
        int[] head = knots[index - 1];
        int[] tail = knots[index];
        // Simulate stretch. Assumes only change of 1 applied at a time.
        if ((Math.abs(head[0] - tail[0]) + Math.abs(head[1] - tail[1])) > 1) {
            // If out of alignment in x and y, move diagonally
            if ((Math.abs(head[0] - tail[0]) + Math.abs(head[1] - tail[1])) > 2) {
                if (head[0] > tail[0]) {
                    tail[0] += 1;
                } else {
                    tail[0] -= 1;
                }
                if (head[1] > tail[1]) {
                    tail[1] += 1;
                } else {
                    tail[1] -= 1;
                }
            } else if (Math.abs(head[0] - tail[0]) > 1) {
                if (head[0] > tail[0]) {
                    tail[0] += 1;
                } else {
                    tail[0] -= 1;
                }
            } else if (Math.abs(head[1] - tail[1]) > 1) {
                if (head[1] > tail[1]) {
                    tail[1] += 1;
                } else {
                    tail[1] -= 1;
                }
            }

        }
        if (index == 9) {
            history.add(String.format("%d,%d", tail[0], tail[1]));
        }
        // System.out.format("Head: (%d, %d) tail: (%d, %d)\n", head[0], head[1],
        // tail[0], tail[1]);
    }

    public void applyInstruction(char direction, int distance) {
        int[] head = knots[0];
        for (int i = 0; i < distance; i++) {
            if (direction == 'L') {
                head[0] -= 1;
            } else if (direction == 'R') {
                head[0] += 1;
            } else if (direction == 'D') {
                head[1] -= 1;
            } else if (direction == 'U') {
                head[1] += 1;
            } else {
                System.out.format("Instruction %c not recognised\n", direction);
            }
            for (int j = 1; j < 10; j++) {
                applyKnotStep(j);
            }
        }
    }

    public void applyInstructionListFromFile(String filepath) {
        try {
            File file = new File(filepath);
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] parts = line.split(" ");
                applyInstruction(parts[0].charAt(0), Integer.parseInt(parts[1]));
                // printKnots();
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("Error reading input file");
            e.printStackTrace();
        }
    }
}