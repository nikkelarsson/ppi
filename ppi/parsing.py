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
        self.invalid_args: object = None
        self.opts_long: object = (
                arg for arg in self.args if arg.startswith("--")
                )
        self.opts_short: object = (
                arg for arg in self.args
                if not arg.startswith("--") and arg.startswith("-")
                )
        self.pos_args: object = (
                arg for index, arg in enumerate(self.args)
                if not arg.startswith("-") and index is not 0
                )

        # This section is temporary – it is here for now
        # so that we can test that the program works.
        for i in self.opts_long:
            print("Long arg: %s" % i)
        for i in self.opts_short:
            print("Short arg: %s" % i)
        for i in self.pos_args:
            print("Pos arg: %s" % i)
