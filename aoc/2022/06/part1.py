def find_start_of_content(data: str):
    iterables = []
    for i in range(4):
        data_iterable = iter(data)
        # Create starting offset
        for _ in range(i):
            next(data_iterable)
        iterables.append(data_iterable)
    for i, (a, b, c, d) in enumerate(zip(*iterables)):
        if len(set((a, b, c, d))) == 4:
            return i + 4

if __name__ == "__main__":
    with open("input.txt") as f:
        answer = find_start_of_content(f.read())
    print(f"Day 6 part 1: {answer}")
