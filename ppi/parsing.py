"""Command line argument parsing."""

import sys

from ppi import constants
from ppi import errors
from ppi import texts


class ArgParser:
    """Class for parsing command line arguments."""

    def __init__(self, argv: list, program: str, language: str) -> None:
        """Initial values."""
        self.argv: list = argv
        self.program: str = program
        self.language: str = language

        self.options: dict = {
            "long": None,
            "short": None
        }

        self.arguments: dict = {
            "invalid": None,
            "positional": None
        }

        # Option switches
        self._project: str = ""
        self._help: bool = False
        self._version: bool = False
        self._quiet: bool = False
        self._git: bool = False

    @property
    def project(self) -> str:
        """Gets project's name."""
        return self._project

    @project.setter
    def project(self, value: str) -> None:
        """Sets project's name."""
        if isinstance(value, str):
            self._project = value

    @property
    def help(self) -> bool:
        """Checks if -h or --help is requested."""
        return self._help

    @help.setter
    def help(self, value: bool) -> None:
        """Sets self._help."""
        if value in {True, False}:
            self._help = value

    @property
    def version(self) -> bool:
        """Checks if -V or --version is requested."""
        return self._version

    @version.setter
    def version(self, value: bool) -> None:
        """Sets self._version."""
        if value in {True, False}:
            self._version = value

    @property
    def quiet(self) -> bool:
        """Checks if -q or --quiet is requested."""
        return self._quiet

    @quiet.setter
    def quiet(self, value: bool) -> None:
        """Sets self._quiet."""
        if value in {True, False}:
            self._quiet = value

    @property
    def git(self) -> bool:
        """Checks if -i or --git-init is requested."""
        return self._git

    @git.setter
    def git(self, value: bool) -> None:
        """Sets self._git."""
        if value in {True, False}:
            self._git = value

    def _startswith_hyphens(self, arg: str, count: int) -> bool:
        """Checks if arg starts with count amount of "-"."""
        return arg[0:count] == "-" * count and arg[count] != "-"

    def _sort_args_long(self) -> None:
        """Gathers all '--' prefixed options from sys.argv into one group."""
        self.options["long"] = (
            arg for arg in self.argv if self._startswith_hyphens(arg, 2)
        )

    def _sort_args_short(self) -> None:
        """Gathers all '-' prefixed options from sys.argv into one group."""
        self.options["short"] = (
            arg for arg in self.argv if self._startswith_hyphens(arg, 1)
        )

    def _sort_args_pos(self) -> None:
        """
        Gathers all arguments with no prefixing
        from sys.argv into one group.
        """
        self.arguments["positional"] = (
            arg for index, arg in enumerate(self.argv)
            if not arg.startswith("-") and index != 0
        )

    def _sort_args(self) -> None:
        """Sorts all argument types."""
        self._sort_args_long()
        self._sort_args_short()
        self._sort_args_pos()

    def _parse_args_inv(self) -> None:
        """Prints error for each invalid argument."""
        if self.arguments["invalid"] is not None:
            for arg in self.arguments["invalid"]:
                errors.InvalidArgumentError(self.program, self.language).throw_error(arg)
            sys.exit(constants.EXIT_ERROR)

    def _parse_args_pos(self) -> None:
        """Stores the first non-prefixed argument from sys.argv."""
        # Grab the first non-flag -argument and ignore the rest.
        for arg in self.arguments["positional"]:
            self.project = arg
            break

    def _parse_args_short(self) -> None:
        """Evaluates each '-' prefixed option."""
        for arg in self.options["short"]:
            for index, letter in enumerate(arg):
                if index == 0:
                    continue  # Skip the "-" prefix.
                if letter == "V":
                    self.version = True
                elif letter == "h":
                    self.help = True
                elif letter == "q":
                    self.quiet = True
                elif letter == "i":
                    self.git = True
                else:
                    if self.arguments["invalid"] is None:
                        self.arguments["invalid"] = []
                    self.arguments["invalid"].append(f"-{letter}")

    def _parse_args_long(self) -> None:
        """Evaluates each '--' prefixed option."""
        for index, arg in enumerate(self.options["long"]):
            if arg == "--version":
                self.version = True
            elif arg == "--help":
                self.help = True
            elif arg == "--quiet":
                self.quiet = True
            elif arg == "--git-init":
                self.git = True
            else:
                if self.arguments["invalid"] is None:
                    self.arguments["invalid"] = []
                self.arguments["invalid"].append(arg)

    def parse_args(self) -> None:
        """Parse args and execute actions according to the given options."""
        self._sort_args()
        self._parse_args_pos()
        self._parse_args_short()
        self._parse_args_long()
        self._parse_args_inv()
