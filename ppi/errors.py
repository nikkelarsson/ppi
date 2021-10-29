"""
errors.py -- Program errors.
Author: Niklas Larsson
Date: October 1, 2021
"""

from . import langcodes


def invargerror(lang: str, prname: str, arg: str) -> None:
    """Print error displaying invalid argument `arg`."""
    if lang == langcodes.LANGCODES["FINNISH"]:
        print("{}: virhe: virheellinen argumentti '{}'".format(prname, arg))
    # We can use the same output for all of the different english-variations.
    elif lang.startswith("en_"):
        print("{}: error: invalid argument '{}'".format(prname, arg))


def direxistserror(lang: str, program: str, arg: str) -> None:
    """Print error when project folder already exists."""
    if lang == langcodes.LANGCODES["FINNISH"]:
        print("{}: virhe: kansio '{}' on jo olemassa".format(program, arg))
    # We can use the same output for all of the different english-variations.
    elif lang.startswith("en_"):
        print("{}: error: dir '{}' already exists".format(program, arg))
