from pathlib import Path

from part2 import load_input, SeatingSimulation


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
            "#.LL.LL.L#",
            "#LLLLLL.LL",
            "L.L.L..L..",
            "LLLL.LL.LL",
            "L.LL.LL.LL",
            "L.LLLLL.LL",
            "..L.L.....",
            "LLLLLLLLL#",
            "#.LLLLLL.L",
            "#.LLLLL.L#",
        ]
        expected = [list(string) for string in expected]
        sim.step()
        sim.step()
        assert sim.current == expected

    def test_step_3(self):
        filepath = Path(__file__).parent / "sample_input.txt"
        layout = load_input(filepath)
        sim = SeatingSimulation(layout)
        expected = [
            "#.L#.##.L#",
            "#L#####.LL",
            "L.#.#..#..",
            "##L#.##.##",
            "#.##.#L.##",
            "#.#####.#L",
            "..#.#.....",
            "LLL####LL#",
            "#.L#####.L",
            "#.L####.L#",
        ]
        expected = [list(string) for string in expected]
        sim.step()
        sim.step()
        sim.step()
        assert sim.current == expected

    def test_run(self):
        filepath = Path(__file__).parent / "sample_input.txt"
        layout = load_input(filepath)
        sim = SeatingSimulation(layout)
        assert sim.run() == 26
