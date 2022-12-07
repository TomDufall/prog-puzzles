from part1 import FileSystem, load_input

def part2(filepath: str = "input.txt") -> int:
    shell_output = load_input(filepath)
    filesystem = FileSystem()
    filesystem.apply_commands(shell_output)
    folder_sizes = filesystem.folder_sizes
    free_space = 70000000 - folder_sizes["/"]
    to_free = 30000000 - free_space
    bigger = {name: size for name, size in folder_sizes.items() if size >= to_free}
    return min(bigger.items(), key=lambda item: item[1])[1]

if __name__ == "__main__":
    print(f"Day 7 part 2: {part2()}")
