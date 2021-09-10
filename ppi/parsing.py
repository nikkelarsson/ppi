"""
parsing.py – Gather and parse command line arguments.
Author: Niklas Larsson
Date: September 10, 2021
"""

class Parsing:
    def __init__(self, args: list) -> None:
        self.args: list = args

        # Invalid prefix types, sequences etc. we don't want
        # to accept as prefixes.
        #
        # New chars/sequences can be added here, by making
        # own section for the sequence etc.
        self.invalid_prefixes: dict = {
                "too_many_hyphens": [
                    "-" * index for index, i in enumerate(range(20), 3)
                    ],
                }

    def __str__(self) -> str:
        return f"Args: {self.args}."

    def __repr__(self) -> str:
        return f"Parsing(args={self.args!r})"


class ParseArgs(Parsing):
    def __init__(self, args: list) -> None:
        super().__init__(args)
