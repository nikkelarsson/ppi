"""
errors.py -- Program errors.
Author: Niklas Larsson
Date: October 1, 2021
"""

from . import langcodes


def invargerror(lang: str, prname: str, arg: str) -> None:
    """Print error displaying invalid argument `arg`."""
    if lang == langcodes.FINNISH:
        print("{}: virhe: virheellinen argumentti '{}'".format(prname, arg))
    elif lang == langcodes.ENGLISH:
        print("{}: error: invalid argument '{}'".format(prname, arg))


def direxistserror(lang: str, program: str, arg: str) -> None:
    """Print error when project folder already exists."""
    if lang == langcodes.FINNISH:
        print("{}: virhe: kansio '{}' on jo olemassa".format(program, arg))
    elif lang == langcodes.ENGLISH:
        print("{}: error: dir '{}' already exists".format(program, arg))
