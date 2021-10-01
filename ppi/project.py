"""
project.py -- Create project files.
Author: Niklas Larsson
Date: September 30, 2021
"""

from . import errors
import os
import sys


def makedir(lang: str, program: str, name: str) -> None:
    """Create dirs for a project and it's sourcecode."""
    if os.path.exists(name):
        errors.direxistserror(lang, program, name)
        sys.exit(1)
    os.makedirs("{0}/{0}".format(name), exist_ok=True)


def makesetup(name: str) -> None:
    """Create setup.py -file."""
    pass


def create(lang: str, program: str, prname: str) -> None:
    """Create everything."""
    makedir(lang, program, prname)
