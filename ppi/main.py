"""Simple utility for starting new Python projects quickly."""


import os
import sys

from ppi import parsing


__author__: str = "Niklas Larsson"
__credits__: list = ["Niklas Larsson"]
__version__: str = "1.2.1"
__program__: str = "ppi"


def main(args: list=sys.argv) -> None:
    parser: object = parsing.ArgParser(args, __program__, __version__, os.getenv("LANG"))
    parser.parse_args()


if __name__ == "__main__":
    main()
