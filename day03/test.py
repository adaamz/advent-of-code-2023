from day03.solve import solve_part1


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
