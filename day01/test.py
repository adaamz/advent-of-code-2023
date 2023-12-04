from day01.solve import solve_part1


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
