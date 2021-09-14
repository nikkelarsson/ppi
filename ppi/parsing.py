"""
parsing.py – Gather and parse command line arguments.
Author: Niklas Larsson
Date: September 10, 2021
"""

class BaseParser:
    def dashes_eqt_one(self, arg: str) -> bool:
        dashes: int = 0
        for letter in arg:
            if dashes > 1:
                return False
            if letter == "-":
                dashes += 1
        return True if dashes == 1 else False

    def dashes_eqt_two(self, arg: str) -> bool:
        dashes: int = 0
        for letter in arg:
            if dashes > 2:
                return False
            if letter == "-":
                dashes += 1
        return True if dashes == 2 else False

    def dashes_eq_o_gt_three(self, arg: str) -> bool:
        dashes: int = 0
        for letter in arg:
            if dashes >= 3:
                return True
            if letter == "-":
                dashes += 1
        return False if dashes < 3 else True


class ArgParser(BaseParser):
    def __init__(self, args: list) -> None:
        self.args: list = args
        self.invalid_args: object = None
        self.opts_long: object = None
        self.opts_short: object = None
        self.pos_args: object = None

    def __repr__(self) -> str:
        return f"ArgParser(args={self.args!r})"

    def __str__(self) -> str:
        return f"Args: {self.args[1:]}"

    def sort_args(self) -> None:
        self.invalid_args = (
                arg for arg in self.args
                if arg.startswith("-") and self.dashes_eq_o_gt_three(arg)
                )
        self.opts_long = (
                arg for arg in self.args
                if arg.startswith("-") and self.dashes_eqt_two(arg)
                )
        self.opts_short = (
                arg for arg in self.args
                if arg.startswith("-") and self.dashes_eqt_one(arg)
                )
        self.pos_args = (
                arg for index, arg in enumerate(self.args)
                if not arg.startswith("-") and index is not 0
                )

    def parse_args_short(self) -> None:
        for arg in self.opts_short:
            for index, letter in enumerate(arg):
                if index == 0:
                    continue  # Skip the "-" prefix.
                for flag in VALID_FLAGS["short"].keys():
                    if letter == flag:
                        pass

    def parse_args_long(self) -> None:
        for arg in self.opts_long:
            pass

    def parse_args(self) -> None:
        if self.opts_short:
            self.parse_args_short()
        if self.opts_long:
            self.parse_args_long()
