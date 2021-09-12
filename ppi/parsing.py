"""
parsing.py – Gather and parse command line arguments.
Author: Niklas Larsson
Date: September 10, 2021
"""

class BaseParser:
    def __str__(self) -> str:
        return f"Args: {self.args}."

    def __repr__(self) -> str:
        return f"Parsing(args={self.args!r})"


class ArgParser(BaseParser):
    def __init__(self, args: list) -> None:
        self.args: list = args

        # Sort arguments into their own categories.
        self.opts_long: object = (
                arg for arg in self.args
                if arg.startswith("--")
                )
        self.opts_short: object = (
                arg for arg in self.args
                if arg.startswith("-")
                )
