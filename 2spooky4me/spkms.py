from itertools import *
import sys


def f(s, x):
    return "".join(
        str(eval(v + x.replace("^", "**").replace("/", "//")))
        if ((v := "".join(g)).isdecimal())
        else v
        for _, g in groupby(s, str.isalpha)
    )


if __name__ == "__main__":
    print(f(sys.argv[1], sys.argv[2]))
