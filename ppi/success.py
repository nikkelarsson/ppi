"""
success.py -- Success messages.
Author: Niklas Larsson
Date: October 1, 2021
"""

from . import langcodes


def msg(lang: str, program: str, prname: str) -> None:
    """Print success message."""
    if lang == langcodes.FINNISH:
        print("{}: \"{}\" luotu.".format(program, prname))
    elif lang == langcodes.ENGLISH:
        print("{}: \"{}\" created.".format(program, prname))
