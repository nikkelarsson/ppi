"""Program errors."""

from ppi.static import lang_codes


def invargerror(lang: str, prname: str, arg: str) -> None:
    """Print error displaying invalid argument `arg`."""
    if lang == lang_codes.LANGCODES["FINNISH"]:
        print("{}: virhe: virheellinen argumentti '{}'".format(prname, arg))
    if lang.startswith("en_") or lang is None:
        print("{}: error: invalid argument '{}'".format(prname, arg))


def direxistserror(lang: str, program: str, arg: str) -> None:
    """Print error when project folder already exists."""
    if lang == lang_codes.LANGCODES["FINNISH"]:
        print("{}: virhe: kansio '{}' on jo olemassa".format(program, arg))
    if lang.startswith("en_") or lang is None:
        print("{}: error: dir '{}' already exists".format(program, arg))
