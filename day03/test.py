from day03.solve import solve_part1
from day03.solve import solve_part2


def test_example1() -> None:
    example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    assert solve_part1(example) == 4361


def test_example1_border() -> None:
    example = """467..114.
...*.....
..35..633
......#..
617*.....
.....+.58
..592....
......755
...$.*...
.664.598."""

    assert solve_part1(example) == 4361


def test_final1() -> None:
    with open("day03/final.txt", "r") as f:
        result = solve_part1(f.read())
        assert result == 539590


def test_example2() -> None:
    example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    assert solve_part2(example) == 467835


def test_final2() -> None:
    with open("day03/final.txt", "r") as f:
        result = solve_part2(f.read())
        assert result == 80703636
