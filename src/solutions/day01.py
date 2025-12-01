from dataclasses import dataclass
from enum import Enum
from typing import TextIO
from common.solution import SolutionBase


class RotationDirection(Enum):
    Left = "L"
    Right = "R"


@dataclass
class Rotation:
    direction: RotationDirection
    degrees: int

    def end_degrees(self, start_degrees: int) -> int:
        match self.direction:
            case RotationDirection.Left:
                return start_degrees - self.degrees
            case RotationDirection.Right:
                return start_degrees + self.degrees


class Solution(SolutionBase[list[Rotation]]):
    @classmethod
    def parse_input(cls, infile: TextIO) -> list[Rotation]:
        rotations = []

        for line in infile:
            direction = RotationDirection(line[0])
            degrees = int(line[1:])
            rotations.append(Rotation(direction, degrees))

        return rotations

    @classmethod
    def part_01(cls, parsed_input: list[Rotation]) -> object:
        total = 0
        degrees = 50

        for rotation in parsed_input:
            degrees = rotation.end_degrees(degrees) % 100
            if degrees == 0:
                total += 1

        return total

    @classmethod
    def part_02(cls, parsed_input: list[Rotation]) -> object:
        total = 0
        degrees = 50

        for rotation in parsed_input:
            end_degrees = rotation.end_degrees(degrees)
            total += cls.num_crossings(degrees, end_degrees)
            degrees = end_degrees

        return total

    @classmethod
    def num_crossings(cls, start_degrees: int, end_degrees: int) -> int:
        if end_degrees > start_degrees:
            return (end_degrees // 100) - (start_degrees // 100)
        else:
            return cls.num_crossings(-start_degrees, -end_degrees)
