"""
descstr.py -- Description strings.
Author: Niklas Larsson
Date: September 29, 2021
"""

from . import langcodes


def show(name: str, version: str, lang: str) -> None:
    if lang == langcodes.FINNISH:
        print("Käyttö: {} [valitsimet] <nimi>".format(name))
    elif lang == langcodes.ENGLISH:
        print("Usage: {} [options] <name>".format(name))
