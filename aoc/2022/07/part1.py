from dataclasses import dataclass, field
import itertools

@dataclass
class FileSystem:
    """
    Filesystem - folders are dicts, files are integers of their size.
    Could replace both with classes, but probably unnecessary
    """
    tree: dict = field(default_factory=dict)
    # Current Working Directory - Linux acronym
    cwd: str = "/"

    def make_file(self, parent: str, name: str, size: int = None, dir: bool = False) -> None:
        working_dir = self.tree
        for cwd_part in parent.split("/"):
            if cwd_part == "":
                continue
            working_dir = working_dir[cwd_part]
        if dir:
            working_dir[name] = {}
        else:
            working_dir[name] = size


    def apply_command(self, command: str, expected_output: list[str]) -> None:
        if command.startswith("cd"):
            argument = command.split(" ")[-1]
            if argument == "/":
                self.cwd = "/"
            elif argument == "..":
                self.cwd = self.cwd.rsplit("/", 1)[0]
            else:
                self.cwd = f"{self.cwd if self.cwd != '/' else ''}/{argument}"
        elif command == "ls":
            # Parse and apply result
            for a, b in map(lambda s: s.split(), expected_output):
                if a == "dir":
                    self.make_file(self.cwd, b, dir=True)
                else:
                    size, name = int(a), b
                    self.make_file(self.cwd, name, size=size)

    def apply_commands(self, commands: list[str, list[str]]) -> None:
        for command, expected_output in commands:
            self.apply_command(command, expected_output)

    @property
    def folder_sizes(self):
        cache = {}
        def get_folder_size(tree: dict, dir_name: str, cache: dict) -> int:
            working_dir = tree
            for cwd_part in dir_name.split("/"):
                if cwd_part == "":
                    continue
                working_dir = working_dir[cwd_part]
            size = 0
            for key, value in working_dir.items():
                if isinstance(value, int):
                    size += value
                else:
                    # Directory
                    subdir = f"{dir_name if dir_name != '/' else ''}/{key}"
                    dir_size = cache.get(subdir)
                    if not dir_size:
                        dir_size = get_folder_size(tree, subdir, cache)
                    size += dir_size
            cache[dir_name] = size
            return size
        get_folder_size(self.tree, "/", cache)
        return cache


def load_input(filepath: str) -> list[tuple[str, list[str]]]:
    with open(filepath) as f:
        raw_commands = f.read().split("$ ")
    output = []
    for command_output in raw_commands[1:]:
        command, *response = command_output.splitlines()
        output.append((command, response))
    return output

def part1(filepath: str = "input.txt") -> int:
    shell_output = load_input(filepath)
    filesystem = FileSystem()
    filesystem.apply_commands(shell_output)
    folder_sizes = filesystem.folder_sizes
    return sum(size for size in folder_sizes.values() if size <= 100000)

if __name__ == "__main__":
    print(f"Day 7 part 1: {part1()}")
