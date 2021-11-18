"""
main.py: Utility to create new Python -projects with.
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
    parser: object = parsing.ArgParser(args, NAME, VERSION, LANG)
    parser.parse_args()


if __name__ == "__main__":
    main()
