"""Command line argument parsing."""

import sys

from ppi import constants
from ppi import errors
from ppi import files
from ppi import texts


class ArgParser:
    """Class for parsing command line arguments."""

    def __init__(self, args: list, name: str, version: str, lang: str) -> None:
        """Initial values."""
        self.args: list = args
        self.name: str = name
        self.version: str = version
        self.lang: str = lang
        self.project: str = None

        # Different argument groups.
        self.invalid_args: list = None
        self.opts_long: object
        self.opts_short: object
        self.pos_args: object

        # Option switches.
        self.help_requested: bool = False
        self.version_requested: bool = False
        self.quiet_requested: bool = False
        self.git_init_requested: bool = False

    def _startswith_hyphens(self, arg: str, count: int) -> bool:
        """Checks if arg starts with count amount of "-"."""
        return arg[0:count] == "-" * count and arg[count] != "-"

    def _sort_args_long(self) -> None:
        """Gathers all '--' prefixed options from sys.argv into one group."""
        self.opts_long = (
            arg for arg in self.args if self._startswith_hyphens(arg, 2)
        )

    def _sort_args_short(self) -> None:
        """Gathers all '-' prefixed options from sys.argv into one group."""
        self.opts_short = (
            arg for arg in self.args if self._startswith_hyphens(arg, 1)
        )

    def _sort_args_pos(self) -> None:
        """
        Gathers all arguments with no prefixing
        from sys.argv into one group.
        """
        self.pos_args = (
            arg for index, arg in enumerate(self.args)
            if not arg.startswith("-") and index != 0
        )

    def _sort_args(self) -> None:
        """Sorts all argument types."""
        self._sort_args_long()
        self._sort_args_short()
        self._sort_args_pos()

    def _parse_args_inv(self) -> None:
        """Prints error for each invalid argument."""
        if self.invalid_args is not None:
            for arg in self.invalid_args:
                errors.InvalidArgumentError(self.name, self.lang).throw_error(arg)
            sys.exit(constants.EXIT_ERROR)

    def _parse_args_pos(self) -> None:
        """Stores the first non-prefixed argument from sys.argv."""
        # Grab the first non-flag -argument and ignore the rest.
        for arg in self.pos_args:
            self.project = arg
            break

    def _parse_args_short(self) -> None:
        """Evaluates each '-' prefixed option."""
        for arg in self.opts_short:
            for index, letter in enumerate(arg):
                if index == 0:
                    continue  # Skip the "-" prefix.
                if letter == "V":
                    self.version_requested = True
                elif letter == "h":
                    self.help_requested = True
                elif letter == "q":
                    self.quiet_requested = True
                elif letter == "i":
                    self.git_init_requested = True
                else:
                    if self.invalid_args is None:
                        self.invalid_args = []
                    self.invalid_args.append("-{}".format(letter))

    def _parse_args_long(self) -> None:
        """Evaluates each '--' prefixed option."""
        for index, arg in enumerate(self.opts_long):
            if arg == "--version":
                self.version_requested = True
            elif arg == "--help":
                self.help_requested = True
            elif arg == "--quiet":
                self.quiet_requested = True
            elif arg == "--git-init":
                self.git_init_requested = True
            else:
                if self.invalid_args is None:
                    self.invalid_args = []
                self.invalid_args.append(arg)

    def parse_args(self) -> None:
        """Parse args and execute actions according to the given options."""
        self._sort_args()
        self._parse_args_pos()
        self._parse_args_short()
        self._parse_args_long()
        self._parse_args_inv()
