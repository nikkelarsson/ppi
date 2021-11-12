"""
success.py: Success messages.
Author: Niklas Larsson
Date: October 1, 2021
"""

from . import langcodes


def msg(lang: str, program: str, prname: str) -> None:
    """Print success message."""
    if lang == langcodes.LANGCODES["FINNISH"]:
        print("{}: \"{}\" luotu.".format(program, prname))
    if lang.startswith("en_") or lang is None:
        print("{}: \"{}\" created.".format(program, prname))
