from collections import defaultdict


def step(states: dict[int, int], steps: int) -> dict[int, int]:
    new_states: dict[int, int]
    for _ in range(steps):
        new_states = defaultdict(lambda: 0)
        for stage, count in states.items():
            stage -= 1
            if stage == -1:
                new_states[6] += count
                new_states[8] += count
            else:
                new_states[stage] += count
        states = new_states
    return states


def load_input(filepath: str = "input.txt") -> dict[int, int]:
    fish_states: dict[int, int] = defaultdict(lambda: 0)
    with open(filepath) as f:
        for n in f.read().split(","):
            fish_states[int(n)] += 1
    return fish_states


if __name__ == "__main__":
    from datetime import datetime

    start = datetime.now()
    fish_states = load_input()
    end_state = step(fish_states, 80)
    print(f"After 80 days: {sum(end_state.values())}")

    fish_states = load_input()
    end_state = step(fish_states, 256)
    print(f"After 256 days: {sum(end_state.values())}")
    end = datetime.now()
    print(f"Seconds: {(end - start).total_seconds()}")
