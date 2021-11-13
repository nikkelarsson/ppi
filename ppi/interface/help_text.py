"""
help_text.py: Program help text.
Author: Niklas Larsson
Date: September 30, 2021
"""

from ppi import static


def show(name: str, lang: str) -> None:
    if lang == static.langcodes.LANGCODES["FINNISH"]:
        print("\nValitsimet:")
        print("-q,  --quiet...... Älä tulosta mitään stdout:iin.")
        print("-i,  --git-init... Alusta projekti git-repona.")
        print("-h,  --help....... Tulosta tämä viesti.")
        print("-V,  --version.... Tulosta {} versio.".format(name))

    if lang.startswith("en_") or lang is None:
        print("\nOptions:")
        print("-q,  --quiet...... Don't print anything to stdout.")
        print("-i,  --git-init... Initialize project as git-repo.")
        print("-h,  --help....... Print this message.")
        print("-V,  --version.... Print {} version.".format(name))
