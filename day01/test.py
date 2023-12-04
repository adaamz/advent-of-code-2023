from day01.solve import solve_part1
from day01.solve import solve_part2


def test_example1() -> None:
    example = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

    assert solve_part1(example) == 142


def test_final1() -> None:
    with open("day01/final.txt", "r") as f:
        assert solve_part1(f.read()) == 54597


def test_example2() -> None:
    example = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

    assert solve_part2(example) == 281


def test_final2() -> None:
    with open("day01/final.txt", "r") as f:
        assert solve_part2(f.read()) == 54504
