from typing import Protocol


class SolutionBase[TParsed](Protocol):
    parsed_type: type[TParsed]

    @classmethod
    def part_01(cls, parsed_input: TParsed) -> object: ...

    @classmethod
    def part_02(cls, parsed_input: TParsed) -> object: ...
