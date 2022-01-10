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
        """Check if `arg` starts with `count` amount of "-"."""
        return arg[0:count] == "-"*count and arg[count] != "-"

    def _sort_args_long(self) -> None:
        self.opts_long = (
            arg for arg in self.args if self._startswith_hyphens(arg, 2)
        )

    def _sort_args_short(self) -> None:
        self.opts_short = (
            arg for arg in self.args if self._startswith_hyphens(arg, 1)
        )

    def _sort_args_pos(self) -> None:
        self.pos_args = (
            arg for index, arg in enumerate(self.args)
            if not arg.startswith("-") and index != 0
        )

    def _sort_args(self) -> None:
        self._sort_args_long()
        self._sort_args_short()
        self._sort_args_pos()

    def _parse_args_inv(self) -> None:
        if self.invalid_args is not None:
            for arg in self.invalid_args:
                errors.InvalidArgumentError(self.name, self.lang).throw_error(arg)
            sys.exit(constants.EXIT_ERROR)

    def _parse_args_pos(self) -> None:
        # Grab the first non-flag -argument and ignore the rest.
        for arg in self.pos_args:
            self.project = arg
            break

    def _parse_args_short(self) -> None:
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

    def _check_if_args(self) -> None:
        if len(self.args) == 1:
            texts.DescriptionText(
                self.version,
                stream=sys.stderr
            ).display(self.name, self.lang)

            texts.UsageText(
                self.version,
                stream=sys.stderr
            ).display(self.name, self.lang)

            sys.exit(constants.EXIT_ERROR)

    def parse_args(self) -> None:
        """Parse args and execute actions according to the given options."""
        self._check_if_args()
        self._sort_args()
        self._parse_args_pos()
        self._parse_args_short()
        self._parse_args_long()
        self._parse_args_inv()
