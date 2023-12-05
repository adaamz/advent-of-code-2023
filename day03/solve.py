from collections import defaultdict
from math import prod
from typing import Optional


def solve_part1(input: str) -> int:
    lines = input.splitlines()

    def _check_numbers(line_id: int, start_numbers_index: int, end_numbers_index: int) -> bool:
        for y in range(max(line_id - 1, 0), min(len(lines) - 1, line_id + 1) + 1):
            for x in range(max(start_numbers_index - 1, 0), min(len(lines[line_id]) - 1, end_numbers_index + 1) + 1):
                if not lines[y][x].isdigit() and lines[y][x] != ".":
                    return True

        return False

    not_abandoned_numbers = []

    for y, line in enumerate(lines):
        start_numbers = None
        end_numbers = None

        for x, c in enumerate(line):
            if c.isdigit() or (x == len(line) - 1 and start_numbers is not None and end_numbers is None):
                if start_numbers is None:
                    start_numbers = x
                else:
                    end_numbers = x

                    if x == len(line) - 1:
                        if _check_numbers(y, start_numbers, end_numbers):
                            number = line[start_numbers: end_numbers + 1]
                            not_abandoned_numbers.append(int("".join(number)))
            else:
                if start_numbers is not None and end_numbers is None:
                    end_numbers = x-1

                if start_numbers is not None and end_numbers is not None:
                    if _check_numbers(y, start_numbers, end_numbers):
                        number = line[start_numbers: end_numbers + 1]
                        not_abandoned_numbers.append(int("".join(number)))

                start_numbers = None
                end_numbers = None

    return sum(not_abandoned_numbers)


def solve_part2(input: str) -> int:

    lines = input.splitlines()

    def _find_star(line_id: int, start_numbers_index: int, end_numbers_index: int) -> Optional[tuple[int, int]]:
        for y in range(max(line_id - 1, 0), min(len(lines) - 1, line_id + 1) + 1):
            for x in range(max(start_numbers_index - 1, 0), min(len(lines[line_id]) - 1, end_numbers_index + 1) + 1):
                if lines[y][x] == "*":
                    return y, x

        return None

    numbers_with_star = defaultdict(list)

    for y, line in enumerate(lines):
        start_numbers = None
        end_numbers = None

        for x, c in enumerate(line):
            if c.isdigit() or (x == len(line) - 1 and start_numbers is not None and end_numbers is None):
                if start_numbers is None:
                    start_numbers = x
                else:
                    end_numbers = x

                    if x == len(line) - 1:
                        if (star := _find_star(y, start_numbers, end_numbers)) is not None:
                            number = line[start_numbers: end_numbers + 1]
                            numbers_with_star[f"{star[0]}-{star[1]}"].append(int("".join(number)))
            else:
                if start_numbers is not None and end_numbers is None:
                    end_numbers = x-1

                if start_numbers is not None and end_numbers is not None:
                    if (star := _find_star(y, start_numbers, end_numbers)) is not None:
                        number = line[start_numbers: end_numbers + 1]
                        numbers_with_star[f"{star[0]}-{star[1]}"].append(int("".join(number)))

                start_numbers = None
                end_numbers = None

    has_two_numbers = filter(
        lambda numbers: len(numbers) == 2, numbers_with_star.values()
    )
    product_numbers = map(prod, has_two_numbers)
    return sum(product_numbers)
