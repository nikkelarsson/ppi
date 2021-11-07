"""
descstr.py -- Description strings.
Author: Niklas Larsson
Date: September 29, 2021
"""

from . import langcodes


def show(name: str, version: str, lang: str) -> None:
    if lang == langcodes.LANGCODES["FINNISH"]:
        print("Käyttö: {} [valitsimet] <nimi>".format(name))
    if lang.startswith("en_") or lang is None:
        print("Usage: {} [options] <name>".format(name))
