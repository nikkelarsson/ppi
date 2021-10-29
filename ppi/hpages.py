"""
hpages.py -- Help pages.
Author: Niklas Larsson
Date: September 30, 2021
"""

from . import langcodes


def show(name: str, lang: str) -> None:
    if lang == langcodes.LANGCODES["FINNISH"]:
        print("\nValitsimet:")
        print("-q,  --quiet...... Älä tulosta mitään stdout:iin.")
        print("-i,  --git-init... Alusta projekti git-repona.")
        print("-h,  --help....... Tulosta tämä viesti.")
        print("-V,  --version.... Tulosta {} versio.".format(name))

    # We can use the same output for all of the different english-variations.
    elif lang.startswith("en_"):
        print("\nOptions:")
        print("-q,  --quiet...... Don't print anything to stdout.")
        print("-i,  --git-init... Initialize project as git-repo.")
        print("-h,  --help....... Print this message.")
        print("-V,  --version.... Print {} version.".format(name))
