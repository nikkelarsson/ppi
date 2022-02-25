"""Help and info texts etc."""

from colorama import Fore
from colorama import Style
from colorama import init
from colorama import deinit
import sys


class Stream:
    """Provides a functionality to easily select to which stream to print."""

    def __init__(self) -> None:
        """Initializes the default stream to use."""
        self._stream: object = sys.stdout

    @property
    def stream(self) -> object:
        """Gets the stream."""
        return self._stream

    @stream.setter
    def stream(self, value: object) -> None:
        """Sets the stream."""
        if value in {sys.stdout, sys.stderr}:
            self._stream = value


class Text:
    """Base class for all Text classes."""

    def __init__(self) -> None:
        """
        Set up switch that text producers can use to change stream they're
        printing to.
        """
        self._switch: Stream = Stream()

    @property
    def switch(self) -> Stream:
        """Get stream switch."""
        return self._switch


class HelpTextFinnish(Text):
    """Help producer for finnish."""

    def __init__(self, program: str) -> None:
        super().__init__()

        self._text: list[str] = [
            "",
            "Valitsimet:",
            "  -a,  --annotate... Generoi lähdetiedostot tyyppiviittauksilla.",
            "  -q,  --quiet...... Älä tulosta mitään stdout:iin.",
            "  -i,  --git-init... Alusta projekti git repona.",
            "  -h,  --help....... Tulosta tämä viesti.",
            "  -V,  --version.... Tulosta {} versio.".format(program),
        ]

    def display(self) -> None:
        """Display help text in finnish."""
        for line in self._text:
            print(line, file=self._switch.stream)


class HelpTextEnglish(Text):
    """Help producer for english."""

    def __init__(self, program: str) -> None:
        super().__init__()

        self._text: list[str] = [
            "",
            "Options:",
            "-a,  --annotate... Generate source files with type hints.",
            "-q,  --quiet...... Don't print anything to stdout.",
            "-i,  --git-init... Initialize project as git-repo.",
            "-h,  --help....... Print this message.",
            "-V,  --version.... Print {} version.".format(program),
        ]

    def display(self) -> None:
        """Display help text in english."""
        for line in self._text:
            print(line, file=self._switch.stream)


class DescriptionTextFinnish(Text):
    """Description producer for finnish."""

    def __init__(self, program: str, version: str) -> None:
        super().__init__()
        message: str = "python projekti generaattori."
        self._desc: str = f"{program} {version}, {message}"

    def display(self) -> None:
        """Display description in finnish."""
        print(self._desc, file=self._switch.stream)


class DescriptionTextEnglish(Text):
    """Description producer for english."""

    def __init__(self, program: str, version: str) -> None:
        super().__init__()
        message: str = "python project generator."
        self._desc: str = f"{program} {version}, {message}"

    def display(self) -> None:
        """Display description in english."""
        print(self._desc, file=self._switch.stream)


class UsageTextFinnish(Text):
    """Usage producer for finnish."""

    def __init__(self, program: str) -> None:
        super().__init__()
        self._message: str = f"Käyttö: {program} [valitsimet] <nimi>"

    def display(self) -> None:
        """Display usage text in finnish."""
        print(self._message, file=self._switch.stream)


class UsageTextEnglish(Text):
    """Usage producer for english."""

    def __init__(self, program: str) -> None:
        super().__init__()
        self._message: str = f"Usage: {program} [options] <name>"

    def display(self) -> None:
        """Display usage text in english."""
        print(self._message, file=self._switch.stream)


class SuccessTextFinnish(Text):
    """Success producer for finnish."""

    def __init__(self, program: str, project: str) -> None:
        super().__init__()
        msg: str = f'{program}: "{project}" luotu! ✨✨'
        self._txt: str = "".join([Fore.YELLOW, Style.BRIGHT, msg])

    def display(self) -> None:
        """Display success in finnish."""
        init(autoreset=True)
        print(self._txt, file=self._switch.stream)
        deinit()


class SuccessTextEnglish(Text):
    """Success producer for english."""

    def __init__(self, program: str, project: str) -> None:
        super().__init__()
        msg: str = f'{program}: "{project}" created! ✨✨'
        self._txt: str = "".join([Fore.YELLOW, Style.BRIGHT, msg])

    def display(self) -> None:
        """Display success in english."""
        init(autoreset=True)
        print(self._txt, file=self._switch.stream)
        deinit()
