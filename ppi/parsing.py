"""
parsing.py: Gather and parse command line arguments.
Author: Niklas Larsson
Date: September 10, 2021
"""

from ppi.interface import desc_text
from ppi.interface import errors
from ppi.interface import file_operation
from ppi.interface import git_operation
from ppi.interface import help_text
from ppi.interface import success_text
from ppi.interface import usage_text

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

    def startswith_hyphens(self, arg: str, count: int) -> bool:
        """Check if `arg` starts with `count` amount of "-"."""
        return arg[0:count] == "-"*count and arg[count] != "-"


class ArgParser(BasicEvalMethods):
    """Class to parse cmd line args with."""
    def __init__(self, args: list, name: str, version: str, lang: str) -> None:
        self.args: list = args
        self.name: str = name
        self.version: str = version
        self.lang: str = lang
        self.prname: str = None

        # Different argument groups.
        self.invalid_args: list = None
        self.opts_long: object
        self.opts_short: object
        self.pos_args: object

        # Option switches.
        self.help_on: bool = False
        self.version_on: bool = False
        self.quiet_on: bool = False
        self.ghrepo_on: bool = False

    def __repr__(self) -> str:
        return f"ArgParser(args={self.args!r})"

    def __str__(self) -> str:
        return f"Args: {self.args[1:]}"

    def sort_args_long(self) -> None:
        self.opts_long = (
                arg for arg in self.args if self.startswith_hyphens(arg, 2)
                )

    def sort_args_short(self) -> None:
        self.opts_short = (
                arg for arg in self.args if self.startswith_hyphens(arg, 1)
                )

    def sort_args_pos(self) -> None:
        self.pos_args = (
                arg for index, arg in enumerate(self.args)
                if not arg.startswith("-") and index != 0
                )

    def sort_args(self) -> None:
        self.sort_args_long()
        self.sort_args_short()
        self.sort_args_pos()

    def parse_args_inv(self) -> None:
        if self.invalid_args is not None:
            for arg in self.invalid_args:
                interface.errors.invargerror(self.lang, self.name, arg)
            sys.exit(1)

    def parse_args_pos(self) -> None:
        # Grab the first non-flag -argument and ignore the rest.
        for arg in self.pos_args:
            self.prname = arg
            break

    def parse_args_short(self) -> None:
        for arg in self.opts_short:
            for index, letter in enumerate(arg):
                if index == 0:
                    continue  # Skip the "-" prefix.
                if letter == "V":
                    self.version_on = True
                elif letter == "h":
                    self.help_on = True
                elif letter == "q":
                    self.quiet_on = True
                elif letter == "i":
                    self.ghrepo_on = True
                else:
                    if self.invalid_args is None:
                        self.invalid_args = []
                    self.invalid_args.append("-{}".format(letter))

    def parse_args_long(self) -> None:
        for index, arg in enumerate(self.opts_long):
            if arg == "--version":
                self.version_on = True
            elif arg == "--help":
                self.help_on = True
            elif arg == "--quiet":
                self.quiet_on = True
            elif arg == "--git-init":
                self.ghrepo_on = True
            else:
                if self.invalid_args is None:
                    self.invalid_args = []
                self.invalid_args.append(arg)

    def check_if_args(self) -> None:
        if len(self.args) == 1:
            interface.usage_text.show(self.name, self.version, self.lang)
            interface.desc_text.show(self.name, self.version, self.lang)
            sys.exit(1)

    def parse_args(self) -> None:
        """Parse args and execute actions according to the given options."""
        self.check_if_args()
        self.sort_args()
        self.parse_args_pos()
        self.parse_args_short()
        self.parse_args_long()
        self.parse_args_inv()
        self.exec_actions()

    def exec_actions(self) -> None:
        if self.help_on:
            interface.usage_text.show(self.name, self.version, self.lang)
            interface.desc_text.show(self.name, self.version, self.lang)
            interface.help_text.show(self.name, self.lang)
            sys.exit(0)
        if self.version_on and not self.help_on:
            interface.usage_text.show(self.name, self.version, self.lang)
            sys.exit(0)
        if self.prname is not None:
            interface.file_operation.create(self.lang, self.name, self.prname)
            if self.ghrepo_on:
                interface.git_operation.git_init(self.prname)
            if not self.quiet_on:
                interface.success_text.msg(self.lang, self.name, self.prname)
            sys.exit(0)
        else:
            interface.usage_text.show(self.name, self.version, self.lang)
            interface.desc_text.show(self.name, self.version, self.lang)
