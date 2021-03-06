"""Help and info texts etc."""

import abc
import colorama
import sys
from ppi import constants


class Text(abc.ABC):
    """Base class for all the subclasses."""

    @abc.abstractmethod
    def display(self, program: str, language: str, stream: object) -> None:
        """
        Prototype method for displaying text.

        Parameters:
            program... Program's name which some fields need in the text output.
            language.. Language in which to display text.
            stream.... Stream where to print output (stdout or stderr).
        """
        pass


class HelpText(Text):
    """Help producer for producing the help text in various languages."""

    def display(self, program: str, language: str, stream: object) -> None:
        """
        Displays help text.

        Parameters:
            program... Program's name which some fields need in the text output.
            language.. Language in which to display text.
        """
        if language == constants.LANG_CODES["FINNISH"]:
            print(file=stream)
            print("Valitsimet:", file=stream)
            print("-a,  --annotate... Generoi lähdetiedostot tyyppiviittauksilla.", file=stream)
            print("-q,  --quiet...... Älä tulosta mitään stdout:iin.", file=stream)
            print("-i,  --git-init... Alusta projekti git-repona.", file=stream)
            print("-h,  --help....... Tulosta tämä viesti.", file=stream)
            print(f"-V,  --version.... Tulosta {program} versio.", file=stream)
        else:
            print(file=stream)
            print("Options:", file=stream)
            print("-a,  --annotate... Generate source files with type hints.", file=stream)
            print("-q,  --quiet...... Don't print anything to stdout.", file=stream)
            print("-i,  --git-init... Initialize project as git-repo.", file=stream)
            print("-h,  --help....... Print this message.", file=stream)
            print(f"-V,  --version.... Print {program} version.", file=stream)


class DescriptionText(Text):
    """
    Description text producer for producing the program
    description text in various languages.
    """

    def __init__(self, version: str) -> None:
        """Description text dependent values."""
        self.version: str = version

    def display(self, program: str, language: str, stream: object) -> None:
        """
        Displays program description text.

        Parameters:
            program... Program's name to display in the description text.
            language.. Language in which to display text.
        """
        msg: str
        if language == constants.LANG_CODES["FINNISH"]:
            msg = f"{program} {self.version}, python projektien alustaja."
            print(msg, file=stream)

        else:
            msg = f"{program} {self.version}, python project initializer."
            print(msg, file=stream)


class UsageText(Text):
    """
    Usage text producer for producing the program usage
    text in various languages.
    """

    def display(self, program: str, language: str, stream: object) -> None:
        """
        Displays program usage text.

        Parameters:
            program... Program's name to display in the usage text.
            language.. Language in which to display text.
        """
        if language == constants.LANG_CODES["FINNISH"]:
            print(f"Käyttö: {program} [valitsimet] <nimi>", file=stream)
        else:
            print(f"Usage: {program} [options] <name>", file=stream)


class SuccessText(Text):
    """Success text producer for producing success text in various languages."""

    def __init__(self, project: str) -> None:
        """Success text dependent values."""
        self.project: str = project

    def display(self, program: str, language: str, stream: object) -> None:
        """
        Displays program success text.

        Parameters:
            program... Program's name to display in the success text.
            language.. Language in which to display text.
        """
        colorama.init(autoreset=True)

        if language == constants.LANG_CODES["FINNISH"]:
            print("".join([
                colorama.Fore.YELLOW,
                colorama.Style.BRIGHT,
                f"{program}: \"{self.project}\" luotu! ✨✨"
            ]), file=stream)

        else:
            print("".join([
                colorama.Fore.YELLOW,
                colorama.Style.BRIGHT,
                f"{program}: \"{self.project}\" created! ✨✨"
            ]), file=stream)

        colorama.deinit()
