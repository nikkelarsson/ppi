"""
success.py -- Success messages.
Author: Niklas Larsson
Date: October 1, 2021
"""

from . import langcodes


def msg(lang: str, program: str, prname: str) -> None:
    """Print success message."""
    if lang == langcodes.LANGCODES["FINNISH"]:
        print("{}: \"{}\" luotu.".format(program, prname))
    # We can use the same output for all of the different english-variations.
    elif lang.startswith("en_"):
        print("{}: \"{}\" created.".format(program, prname))
