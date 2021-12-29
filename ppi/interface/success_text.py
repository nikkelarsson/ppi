"""Program success text."""


import colorama
import sys

from ppi.static import lang_codes


def msg(lang: str, program: str, prname: str) -> None:
    """Indicate a successful initalization by printing informative message."""
    colorama.init(autoreset=True)

    if lang == lang_codes.LANGCODES["FINNISH"]:
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
