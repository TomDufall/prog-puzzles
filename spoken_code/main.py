# https://en.wikipedia.org/wiki/Look-and-say_sequence


def gen_next(prev=""):
    if not prev:
        return "1"
    elif len(prev) == 1:
        return f"1{prev}"
    else:
        a = prev[0]
        count = 1
        result = ""
        for digit in prev[1:]:
            # print(f"{a=}, {digit=}, {count=}, {result=}")
            if digit == a:
                count += 1
                continue
            else:
                result += f"{count}{a}"
                a = digit
                count = 1
        result += f"{count}{a}"
        return result


if __name__ == "__main__":
    result = None
    for _ in range(15):
        result = gen_next(result)
        print(result)
