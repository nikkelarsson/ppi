"""
usgstr.py -- Usage strings.
Author: Niklas Larsson
Date: September 29, 2021
"""

from . import langcodes


def show(name: str, version: str, lang: str) -> None:
    if lang == langcodes.FINNISH:
        print("{} {}, python projektien alustaja.".format(name, version))
    elif lang == langcodes.ENGLISH:
        print("{} {}, python project initializer.".format(name, version))
