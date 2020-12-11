from pathlib import Path

from part1 import load_input, SeatingSimulation


class TestSeatingSimulation:
    def test_step(self):
        filepath = Path(__file__).parent / "sample_input.txt"
        layout = load_input(filepath)
        sim = SeatingSimulation(layout)
        expected = [
            "#.##.##.##",
            "#######.##",
            "#.#.#..#..",
            "####.##.##",
            "#.##.##.##",
            "#.#####.##",
            "..#.#.....",
            "##########",
            "#.######.#",
            "#.#####.##",
        ]
        expected = [list(string) for string in expected]
        sim.step()
        assert sim.current == expected

    def test_step_2(self):
        filepath = Path(__file__).parent / "sample_input.txt"
        layout = load_input(filepath)
        sim = SeatingSimulation(layout)
        expected = [
            "#.LL.L#.##",
            "#LLLLLL.L#",
            "L.L.L..L..",
            "#LLL.LL.L#",
            "#.LL.LL.LL",
            "#.LLLL#.##",
            "..L.L.....",
            "#LLLLLLLL#",
            "#.LLLLLL.L",
            "#.#LLLL.##",
        ]
        expected = [list(string) for string in expected]
        sim.step()
        sim.step()
        assert sim.current == expected

    def test_run(self):
        filepath = Path(__file__).parent / "sample_input.txt"
        layout = load_input(filepath)
        sim = SeatingSimulation(layout)
        assert sim.run() == 37
