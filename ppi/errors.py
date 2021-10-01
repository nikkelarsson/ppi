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
