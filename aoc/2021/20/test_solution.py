from solution import apply_algorithm_n, count_lit_pixels, get_neighbours, load_input


def test_get_neighbours():
    image = [
        ["#", ".", ".", "#", "."],
        ["#", ".", ".", ".", "."],
        ["#", "#", ".", ".", "#"],
        [".", ".", "#", ".", "."],
        [".", ".", "#", "#", "#"],
    ]
    point = (0, 1)
    expected = [[".", "#", "."], [".", "#", "."], [".", "#", "#"]]
    assert get_neighbours(point, image, ".") == expected


def test_load_input():
    expected_algorithm = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
    expected_image = [
        ["#", ".", ".", "#", "."],
        ["#", ".", ".", ".", "."],
        ["#", "#", ".", ".", "#"],
        [".", ".", "#", ".", "."],
        [".", ".", "#", "#", "#"],
    ]
    actual_algorithm, actual_image = load_input("sample_input.txt")
    assert actual_algorithm == expected_algorithm
    assert actual_image == expected_image


def test_full():
    expected_lit = 35
    algorithm, image = load_input("sample_input.txt")
    end_image = apply_algorithm_n(algorithm, image, 2)
    actual_lit = count_lit_pixels(end_image)
    assert actual_lit == expected_lit
