"""
success_text.py: Program success text.
Author: Niklas Larsson
Date: October 1, 2021
"""


from ppi.static import lang_codes


def msg(lang: str, program: str, prname: str) -> None:
    """Print success message."""
    if lang == lang_codes.LANGCODES["FINNISH"]:
        print("{}: \"{}\" luotu.".format(program, prname))
    if lang.startswith("en_") or lang is None:
        print("{}: \"{}\" created.".format(program, prname))
