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
        if self.language == constants.LANG_CODES["FINNISH"]:
            print(
                f"{self.program}: virhe: virheellinen argumentti '{arg}'",
                file=sys.stderr
            )

        else:
            print(
                f"{self.program}: error: invalid argument '{arg}'",
                file=sys.stderr
            )
