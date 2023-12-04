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
