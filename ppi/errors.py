"""Program errors."""

import abc
import sys

from ppi import constants


class Error(abc.ABC):
    """Base class for all the different error classes."""

    @abc.abstractmethod
    def throw_error(self, arg: str) -> None:
        """
        Prototype method for throwing errors.

        Parameters:
            arg.... The argument that is invalid.
        """
        pass


class BadArgumentErrorFinnish:
    """For handling invalid arguments in finnish."""

    def __init__(self, args: list) -> None:
        # Truncate arguments if there was many invalid ones
        fmtd: str = ""
        if len(args) > 8:
            fmtd = ", ".join(args[0:8])
            fmtd += "..."
        else:
            fmtd = ", ".join(args)

        self._msg: str = ""
        if len(args) > 1:
            self._msg = f"Virhe: tuntemattomia argumentteja '{fmtd}'"
        if len(args) == 1:
            self._msg = f"Virhe: tuntematon argumentti '{fmtd}'"

    def throw(self) -> None:
        """Display error message in finnish."""
        print(self._msg, file=sys.stderr)


class BadArgumentErrorEnglish:
    """For handling invalid arguments in english."""

    def __init__(self, args: list) -> None:
        # Truncate arguments if there was many invalid ones
        fmtd: str = ""
        if len(args) > 8:
            fmtd = ", ".join(args[0:8])
            fmtd += "..."
        else:
            fmtd = ", ".join(args)

        self._msg: str = ""
        if len(args) > 1:
            self._msg = f"Error: unknown arguments '{fmtd}'"
        if len(args) == 1:
            self._msg = f"Error: unknown argument '{fmtd}'"

    def throw(self) -> None:
        """Display error message in english."""
        print(self._msg, file=sys.stderr)


class ExtraArgumentErrorFinnish:
    """For handling extra arguments in finnish."""

    def __init__(self, args: list) -> None:
        # Truncate arguments if there was many extra ones
        fmtd: str = ""
        if len(args) > 8:
            fmtd = ", ".join(args[0:8])
            fmtd += "..."
        else:
            fmtd = ", ".join(args)

        self._msg: str = ""
        if len(args) > 1:
            self._msg = f"Virhe: ylimääräisiä argumentteja '{fmtd}'"
        if len(args) == 1:
            self._msg = f"Virhe: ylimääräinen argumentti '{fmtd}'"

    def throw(self) -> None:
        """Display error message in finnish."""
        print(self._msg, file=sys.stderr)


class ExtraArgumentErrorEnglish:
    """For handling extra arguments in english."""

    def __init__(self, args: list) -> None:
        # Truncate arguments if there was many extra ones
        fmtd: str = ""
        if len(args) > 8:
            fmtd = ", ".join(args[0:8])
            fmtd += "..."
        else:
            fmtd = ", ".join(args)

        self._msg: str = ""
        if len(args) > 1:
            self._msg = f"Error: extra arguments '{fmtd}'"
        if len(args) == 1:
            self._msg = f"Error: extra argument '{fmtd}'"

    def throw(self) -> None:
        """Display error message in english."""
        print(self._msg, file=sys.stderr)


class InvalidArgumentError(Error):
    """Class for handling invalid argument errors."""

    def __init__(self, program: str, language: str) -> None:
        """
        Values specific to InvalidArgumentError.

        Parameters:
            program... Program's name for displaying it in the error message.
            language.. Language in which to display error message.
        """
        self.program: str = program
        self.language: str = language

    def throw_error(self, arg: str) -> None:
        """
        Throws error when invalid argument is encountered on cl.

        Parameters:
            arg.... The argument that is invalid.
        """
        msg: str
        if self.language == constants.LANG_CODES["FINNISH"]:
            msg = f"{self.program}: virhe: virheellinen argumentti '{arg}'"
        else:
            msg = f"{self.program}: error: invalid argument '{arg}'"
        print(msg, file=sys.stderr)


class ExtraArgumentError(Error):
    """Class for handling extra argument errors."""

    def __init__(self, program: str, language: str) -> None:
        """
        Initializes ExtraArgumentError class.

        Parameters:
            program... Program's name for displaying it in the error message.
            language.. Language in which to display error message.
        """
        self.program: str = program
        self.language: str = language

    def throw_error(self, arg: str) -> None:
        """
        Throws error when extra argument is encountered on cl.

        Parameters:
            arg.... The argument that is extra.
        """
        msg: str
        if self.language == constants.LANG_CODES["FINNISH"]:
            msg = f"{self.program}: virhe: ylimääräinen argumentti '{arg}'"
        else:
            msg = f"{self.program}: error: extra argument '{arg}'"
        print(msg, file=sys.stderr)
