from typing import Literal

from cyclopts import run


def get_solution(day: int):
    match day:
        case 1:
            from solutions.day01 import Solution as Solution01

            return Solution01
        case _:
            raise ValueError(f"No solution found for day {day}")


def main(day: int, part: Literal[1, 2], use_example_input: bool = False):
    solution = get_solution(day)

    filename = "example.txt" if use_example_input else "input.txt"
    with open(f"input/day{day:02d}/{filename}", "r") as infile:
        parsed_input = solution.parse_input(infile)

    match part:
        case 1:
            answer = solution.part_01(parsed_input)
        case 2:
            answer = solution.part_02(parsed_input)
        case _:
            raise ValueError(f"Invalid part {part}")

    print(answer)


if __name__ == "__main__":
    run(main)
