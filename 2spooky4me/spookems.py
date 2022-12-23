import operator
from typing import Generator, Union

DIGITS = "0123456789"
OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
    "^": operator.pow,
}


def split_input(text: str) -> Generator[Union[int, str], None, None]:
    temp: str = None
    is_number = False
    for char in text:
        if char in DIGITS:
            if temp is None:
                temp = char
                is_number = True
            elif is_number:
                temp += char
            else:
                # Change from string to number
                yield temp
                temp = char
                is_number = True
        else:
            if temp is None:
                temp = char
                is_number = False
            elif not is_number:
                temp += char
            else:
                # Change from number to string
                yield int(temp)
                temp = char
                is_number = False
    if is_number:
        yield int(temp)
    else:
        yield temp


def change_spookiness(text: str, operation: str) -> str:
    if text == "":
        return ""
    operator = OPERATORS[operation[0]]
    value = int(operation[1:])
    mapper = (
        lambda token: str(operator(token, value)) if isinstance(token, int) else token
    )
    return "".join(map(mapper, split_input(text)))


if __name__ == "__main__":
    # Note: if invoking with GitBash, specify a "/" arg as "//" to avoid
    # filepath expansion. Nothing to do with Python.
    import sys

    print(change_spookiness(sys.argv[1], sys.argv[2]))
