"""
errors.py -- Program errors.
Author: Niklas Larsson
Date: October 1, 2021
"""

from . import langcodes


def inargerror(lang: str, prname: str, arg: str) -> None:
    """Print error displaying invalid argument `arg`."""
    if lang == langcodes.FINNISH:
        print("{}: virhe: virheellinen argumentti '{}'".format(name, arg))
    elif lang == langcodes.ENGLISH:
        print("{}: error: invalid argument '{}'".format(name, arg))
