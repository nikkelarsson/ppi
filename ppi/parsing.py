"""Command line argument parsing."""

import sys

from ppi import constants
from ppi import errors
from ppi import texts


class ArgumentParser:
    """Class for parsing command line arguments."""

    def __init__(self, program: str, language: str) -> None:
        """Initial values."""
        self.argv: list = sys.argv
        self.argc: int = len(self.argv)
        self.program: str = program
        self.language: str = language

        self.options: dict = {
            "long": None,
            "short": None
        }

        self.arguments: dict = {
            "invalid": None,
            "positional": None,
            "extra": None
        }

        # Option switches
        self._args: bool = self.argc >= 2
        self._project: str = ""
        self._help: bool = False
        self._version: bool = False
        self._quiet: bool = False
        self._git: bool = False
        self._annotate: bool = False

    @property
    def args(self) -> bool:
        """Gets whether anough args were provided on the command line."""
        return self._args

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

    @property
    def annotate(self) -> bool:
        """Gets whether -a or --annotate was provided on the command line."""
        return self._annotate

    @annotate.setter
    def annotate(self, value: bool) -> None:
        """Sets self._annotate."""
        if value in {True, False}:
            self._annotate = value

    @property
    def invargs(self) -> list:
        """Get invalid arguments."""
        if self.arguments["invalid"] is not None:
            return self.arguments["invalid"]

        return []

    @property
    def xargs(self) -> list:
        """Get extra arguments."""
        if self.arguments["extra"] is not None:
            return self.arguments["extra"]

        return []

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
            handler: object = errors.InvalidArgumentError(
                self.program,
                self.language
            )
            for arg in self.arguments["invalid"]:
                handler.throw_error(arg)
            del handler
            sys.exit(constants.EXIT_ERROR)

    def _parse_args_xtra(self) -> None:
        """Prints error for each xtra positional arguments."""
        if self.arguments["extra"] is not None:
            handler: object = errors.ExtraArgumentError(
                self.program,
                self.language
            )
            for arg in self.arguments["extra"]:
                handler.throw_error(arg)
            del handler
            sys.exit(constants.EXIT_ERROR)

    def _parse_args_pos(self) -> None:
        """Stores the first non-prefixed argument from sys.argv."""
        if self.arguments["positional"]:
            for arg in self.arguments["positional"]:
                if self.project:
                    if self.arguments["extra"] is None:
                        self.arguments["extra"] = []
                    self.arguments["extra"].append(arg)
                else:
                    self.project = arg

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
                elif letter == "a":
                    self.annotate = True
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
            elif arg == "--annotate":
                self.annotate = True
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

        # NOTE: This functionality has been migrated to main.py (or __main__.py)
        # self._parse_args_inv()
        # self._parse_args_xtra()
