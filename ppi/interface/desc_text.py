"""
desc_text.py: Program description text.
Author: Niklas Larsson
Date: September 29, 2021
"""

from ppi.static import langcodes


def show(name: str, version: str, lang: str) -> None:
    if lang == static.langcodes.LANGCODES["FINNISH"]:
        print("{} {}, python projektien alustaja.".format(name, version))
    if lang.startswith("en_") or lang is None:
        print("{} {}, python project initializer.".format(name, version))
