import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static ArrayList<ArrayList<Integer>> loadInput() {
        ArrayList<ArrayList<Integer>> elves = new ArrayList<ArrayList<Integer>>();
        try {
            File file = new File("input.txt");
            Scanner scanner = new Scanner(file);
            elves.add(new ArrayList<Integer>());
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                if (line.isEmpty()) {
                    elves.add(new ArrayList<Integer>());
                } else {
                    elves.get(elves.size() - 1).add(Integer.parseInt(line));
                }
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("Error reading input file");
            e.printStackTrace();
        }
        return elves;
    }

    static ArrayList<Integer> sumCalories(ArrayList<ArrayList<Integer>> elves) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (ArrayList<Integer> elf : elves) {
            int sum = 0;
            for (int item : elf) {
                sum += item;
            }
            result.add(sum);
        }
        return result;
    }

    static int max(ArrayList<Integer> ints) {
        int max = ints.get(0);
        for (int number : ints) {
            if (number > max) {
                max = number;
            }
        }
        return max;
    }

    static int sumTopThree(ArrayList<Integer> ints) {
        int maxOne = 0;
        int maxTwo = 0;
        int maxThree = 0;
        for (int number : ints) {
            if (number > maxOne) {
                maxThree = maxTwo;
                maxTwo = maxOne;
                maxOne = number;
            } else if (number > maxTwo) {
                maxThree = maxTwo;
                maxTwo = number;
            } else if (number > maxThree) {
                maxThree = number;
            }
        }
        return maxOne + maxTwo + maxThree;
    }

    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> rawElves = loadInput();
        ArrayList<Integer> elfSummaries = sumCalories(rawElves);
        int answerOne = max(elfSummaries);
        System.out.format("Day 1 part 1 Java answer: %d", answerOne);
        int answerTwo = sumTopThree(elfSummaries);
        System.out.format("Day 1 part 2 Java answer: %d", answerTwo);
    }
}