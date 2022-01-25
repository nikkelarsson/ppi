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
            print(msg, file=sys.stderr)

        else:
            msg = f"{self.program}: error: invalid argument '{arg}'"
            print(msg, file=sys.stderr)
