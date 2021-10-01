"""
hpages.py -- Help pages.
Author: Niklas Larsson
Date: September 30, 2021
"""

from . import langcodes


def show(name: str, lang: str) -> None:
    if lang == langcodes.FINNISH:
        print("\nValitsimet:")
        print("-h,  --help....... Tulosta tämä viesti.")
        print("-V,  --version.... Tulosta {} versio.".format(name))
    elif lang == langcodes.ENGLISH:
        print("\nOptions:")
        print("-h,  --help....... Print this message.")
        print("-V,  --version.... Print {} version.".format(name))