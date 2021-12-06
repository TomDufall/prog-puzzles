from typing import Collection, List, Tuple

IntArray2D = List[List[int]]


def calc_score(board: IntArray2D, called: Collection[int]) -> Tuple[int, int]:
    """
    Find the score of a completed board given the last of calls up to where it
    completed.
    The score is the sum of the numbers in the board not called at any time.
    Returns (number of calls, score)
    """
    board_numbers = {n for row in board for n in row}
    return len(called), sum(board_numbers.difference(called))


def score_board(board: IntArray2D, calls: List[int]) -> Tuple[int, int]:
    """
    Find the number of calls when a row or column is completed. The score is
    the sum of the remaining numbers.
    Return (calls to win, score)
    """
    done = False
    for i in range(len(calls)):
        called = set(calls[: i + 1])
        for row in board:
            if set(row).issubset(called):
                done = True
                break
        for col_i in range(len(board[0])):
            col = {row[col_i] for row in board}
            if col.issubset(called):
                done = True
                break
        if done:
            break
    else:
        raise Exception("Unable to complete board")
    return calc_score(board, called)


def load_input(filepath: str = "input.txt") -> Tuple[List[IntArray2D], List[int]]:
    """
    Load input file and return a list of boards and a list of ints called out.
    """
    with open(filepath) as f:
        calls = [int(num) for num in f.readline().split(",")]
        f.readline()  # discard newline
        board_groups = f.read().split("\n\n")
    boards = []
    for group in board_groups:
        board = [
            [int(num) for num in line.strip().split()] for line in group.splitlines()
        ]
        boards.append(board)
    return boards, calls


if __name__ == "__main__":
    boards, calls = load_input()
    scores = {i: score_board(board, calls) for i, board in enumerate(boards)}
    winner = min(scores.items(), key=lambda item: item[1][0])
    print(
        f"Winning board is index {winner[0]}, after {winner[1][0]} calls, score {winner[1][1]}"
    )
    print(f"Part 1 answer is {winner[1][1] * calls[winner[1][0] -1]}")
    # Part 2
    loser = max(scores.items(), key=lambda item: item[1][0])
    print(
        f"Losing board is index {loser[0]}, after {loser[1][0]} calls, score {loser[1][1]}"
    )
    print(f"Part 2 answer is {loser[1][1] * calls[loser[1][0] -1]}")
