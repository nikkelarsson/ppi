"""
usage_text.py: Program usage text.
Author: Niklas Larsson
Date: September 29, 2021
"""


from ppi.static import lang_codes


def show(name: str, version: str, lang: str) -> None:
    if lang == lang_codes.LANGCODES["FINNISH"]:
        print("Käyttö: {} [valitsimet] <nimi>".format(name))
    if lang.startswith("en_") or lang is None:
        print("Usage: {} [options] <name>".format(name))
