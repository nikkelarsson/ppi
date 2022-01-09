"""Help and info texts etc."""

import colorama
import sys
from ppi import constants


def hlp(name: str, lang: str) -> None:
    if lang == constants.LANG_CODES["FINNISH"]:
        print("\nValitsimet:")
        print("-q,  --quiet...... Älä tulosta mitään stdout:iin.")
        print("-i,  --git-init... Alusta projekti git-repona.")
        print("-h,  --help....... Tulosta tämä viesti.")
        print("-V,  --version.... Tulosta {} versio.".format(name))

    if lang.startswith("en_") or lang is None:
        print("\nOptions:")
        print("-q,  --quiet...... Don't print anything to stdout.")
        print("-i,  --git-init... Initialize project as git-repo.")
        print("-h,  --help....... Print this message.")
        print("-V,  --version.... Print {} version.".format(name))


def desc(name: str, version: str, lang: str) -> None:
    if lang == constants.LANG_CODES["FINNISH"]:
        print("{} {}, python projektien alustaja.".format(name, version))
    if lang.startswith("en_") or lang is None:
        print("{} {}, python project initializer.".format(name, version))


def succ(lang: str, program: str, prname: str) -> None:
    """Indicate a successful initalization by printing informative message."""
    colorama.init(autoreset=True)

    if lang == constants.LANG_CODES["FINNISH"]:
        print("".join([
            colorama.Fore.YELLOW,
            colorama.Style.BRIGHT,
            f"{program}: \"{prname}\" luotu! ✨✨"
            ]), file=sys.stderr)

    if lang.startswith("en_") or lang is None:
        print("".join([
            colorama.Fore.YELLOW,
            colorama.Style.BRIGHT,
            f"{program}: \"{prname}\" created! ✨✨"
            ]), file=sys.stderr)

    colorama.deinit()


def usg(name: str, version: str, lang: str) -> None:
    if lang == constants.LANG_CODES["FINNISH"]:
        print("Käyttö: {} [valitsimet] <nimi>".format(name))
    if lang.startswith("en_") or lang is None:
        print("Usage: {} [options] <name>".format(name))
