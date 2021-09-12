"""
main.py – Utility to create new python -projects with.
Author: Niklas Larsson
Date: September 10, 2021
"""


from . import parsing

import sys
import os


LANG: str = os.getenv("LANG")
NAME: str = "ppi"
VERSION: str = "1.0"


def main(args: list=sys.argv) -> None:
    parsed: object = parsing.ArgParser(args)


if (__name__ == "__main__"):
    main()
