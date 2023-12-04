import re

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
