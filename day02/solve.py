import re
from math import prod

limit = {"red": 12, "green": 13, "blue": 14}

def _check_rounds(rounds: list[str]) -> bool:
    for round in rounds:
        bags = round.split(", ")
        for bag in bags:
            count, color = bag.split(" ")
            if limit[color] < int(count):
                return False

    return True

def solve_part1(input: str) -> int:
    game_id_re = re.compile("^Game (\d+):")

    sum = 0

    for line in input.splitlines():
        game_id = int(game_id_re.findall(line)[0])

        rounds = line.removeprefix(f"Game {game_id}: ").split("; ")

        if _check_rounds(rounds):
            sum += game_id

    return sum


def _maximum_rounds(rounds: list[str]) -> dict[str, int]:
    maximum = {color: 0 for color in ["blue", "green", "red"]}

    for round in rounds:
        bags = round.split(", ")
        for bag in bags:
            count, color = bag.split(" ")
            maximum[color] = max(maximum[color], int(count))

    return maximum


def solve_part2(input: str) -> int:
    game_id_re = re.compile("^Game (\d+):")

    result = 0

    for line in input.splitlines():
        game_id = int(game_id_re.findall(line)[0])

        rounds = line.removeprefix(f"Game {game_id}: ").split("; ")

        result += prod(_maximum_rounds(rounds).values())

    return result
