import re


def solve_part1(input: str) -> int:
    re_first_last = re.compile(r"\d")

    lines = input.split("\n")
    sum = 0
    for line in lines:
        matched_numbers = re_first_last.findall(line)
        if not matched_numbers:
            print(line)
            continue

        number = f"{matched_numbers[0]}{matched_numbers[-1]}"
        sum += int(number)

    return sum


def solve_part2(input: str) -> int:
    vocal = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    vocal_reversed = [n[::-1] for n in vocal]

    def find_first(line: str, opposite: bool = False) -> int:
        tmp = ""
        for c in line:
            if c.isdigit():
                return int(c)

            tmp += c
            for k, v in enumerate(vocal if not opposite else vocal_reversed):
                if v in tmp:
                    return int(k)

    lines = input.split("\n")
    sum = 0
    for line in lines:
        number = f"{find_first(line)}{find_first(line[::-1], opposite=True)}"

        sum += int(number)

    return sum
