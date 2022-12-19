public class Main {
    public static void main(String[] args) {
        String filepath;
        if (args.length < 1) {
            filepath = "input.txt";
        } else {
            filepath = args[0];
        }
        RopeSimulation sim = new RopeSimulation();
        sim.applyInstructionListFromFile(filepath);
        System.out.format("Day 9 part 1 Java: %d\n", sim.history.size());

        RopeSimulationImproved sim2 = new RopeSimulationImproved();
        sim2.applyInstructionListFromFile(filepath);
        System.out.format("Day 9 part 2 Java: %d\n", sim2.history.size());

    }
}
