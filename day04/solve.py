import math
import re


def solve_part1(input: str) -> int:
    re_card_id = re.compile(r"^Card[ ]*\d+:[ ]*")
    lines = input.splitlines()

    sum = 0

    for line in lines:
        card_str = re_card_id.findall(line)[0]
        winning_str, elfs_str = line.removeprefix(card_str).replace("  ", " ").split(" | ")
        winning_numbers = set(map(int, winning_str.split(" ")))
        elfs_numbers = set(map(int, elfs_str.split(" ")))

        exp = len(winning_numbers & elfs_numbers)
        if exp > 0:
            sum += int(math.pow(2, exp - 1))

    return sum


def solve_part2(input: str) -> int:
    re_card_id = re.compile(r"^Card[ ]*\d+:[ ]*")
    lines = input.splitlines()

    max_card_id = len(lines)
    card_copies = [1] * max_card_id

    for card_id, line in enumerate(lines):
        card_str = re_card_id.findall(line)[0]
        winning_str, elfs_str = line.removeprefix(card_str).replace("  ", " ").split(" | ")
        winning_numbers = set(map(int, winning_str.split(" ")))
        elfs_numbers = set(map(int, elfs_str.split(" ")))

        matches_count = len(winning_numbers & elfs_numbers)

        for i in range(1, min(matches_count, max_card_id) + 1):
            card_copies[card_id + i] += card_copies[card_id]

    return sum(card_copies)
