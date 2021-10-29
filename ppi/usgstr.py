"""
usgstr.py -- Usage strings.
Author: Niklas Larsson
Date: September 29, 2021
"""

from . import langcodes


def show(name: str, version: str, lang: str) -> None:
    if lang == langcodes.LANGCODES["FINNISH"]:
        print("{} {}, python projektien alustaja.".format(name, version))
    # We can use the same output for all of the different english-variations.
    elif lang.startswith("en_"):
        print("{} {}, python project initializer.".format(name, version))
