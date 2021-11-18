"""
usage_text.py: Program usage text.
Author: Niklas Larsson
Date: September 29, 2021
"""

from ppi.static import langcodes


def show(name: str, version: str, lang: str) -> None:
    if lang == langcodes.LANGCODES["FINNISH"]:
        print("Käyttö: {} [valitsimet] <nimi>".format(name))
    if lang.startswith("en_") or lang is None:
        print("Usage: {} [options] <name>".format(name))
