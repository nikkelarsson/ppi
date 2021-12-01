"""
main.py: Utility to create new Python -projects with.
Author: Niklas Larsson
Date: September 10, 2021
"""


import os
import sys

from ppi import parsing


LANG: str = os.getenv("LANG")
NAME: str = "ppi"
MAJOR: int = 1
MINOR: int = 1
PATCH: int = 0
VERSION: str = "{}.{}.{}".format(MAJOR, MINOR, PATCH)


def main(args: list=sys.argv) -> None:
    parser: object = parsing.ArgParser(args, NAME, VERSION, LANG)
    parser.parse_args()


if __name__ == "__main__":
    main()
