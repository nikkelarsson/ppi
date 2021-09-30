"""
parsing.py -- Gather and parse command line arguments.
Author: Niklas Larsson
Date: September 10, 2021
"""

from . import commands
from . import usgstr
from . import descstr
import sys
from textwrap import dedent


class BasicEvalMethods:
    """Class containing basic eval -funcs to evaluate cmd line options with."""
    def dashes_eqt_one(self, arg: str) -> bool:
        """Check if `arg` contains exactly one hyphen."""
        dashes: int = 0
        for letter in arg:
            if dashes > 1:
                return False
            if letter == "-":
                dashes += 1
        return True if dashes == 1 else False

    def dashes_eqt_two(self, arg: str) -> bool:
        """Check if `arg` contains exactly two hyphens."""
        dashes: int = 0
        for letter in arg:
            if dashes > 2:
                return False
            if letter == "-":
                dashes += 1
        return True if dashes == 2 else False

    def dashes_eq_o_gt_three(self, arg: str) -> bool:
        """Check if `arg` contains three or more hyphens."""
        dashes: int = 0
        for letter in arg:
            if dashes >= 3:
                return True
            if letter == "-":
                dashes += 1
        return False if dashes < 3 else True


class ArgParser(BasicEvalMethods):
    """Class to parse cmd line args with."""
    def __init__(self, args: list, name: str, version: str, lang: str) -> None:
        self.args: list = args
        self.name: str = name
        self.version: str = version
        self.lang: str = lang
        self.description: str = "cool program to make things with."
        self.invalid_args: object
        self.opts_long: object
        self.opts_short: object
        self.pos_args: object
        self.verbose: bool = False
        self.help_requested: bool = False

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
                if not arg.startswith("-") and index != 0
                )

    def parse_args_short(self) -> None:
        for arg in self.opts_short:
            for index, letter in enumerate(arg):
                if index == 0:
                    continue  # Skip the "-" prefix.
                if letter == "V":
                    self.verbose = True
                elif letter == "h":
                    self.help_requested = True

    def parse_args_long(self) -> None:
        for index, arg in enumerate(self.opts_long):
            if index == 0 or index == 1:
                continue  # Skip the "--" prefix.
            elif arg == "--version":
                self.verbose = True
            elif arg == "--help":
                self.help_requested = True

    def check_if_args(self) -> None:
        if len(self.args) == 1:
            usgstr.show(self.name, self.version, self.lang)
            descstr.show(self.name, self.version, self.lang)
            sys.exit(1)

    def parse_args(self) -> None:
        """Parse args and execute actions according to the given options."""
        self.check_if_args()
        self.sort_args()
        self.parse_args_short()
        self.parse_args_long()
        self.exec_actions()

    def exec_actions(self) -> None:
        if self.help_requested:
            pass
        elif self.version:
            pass
