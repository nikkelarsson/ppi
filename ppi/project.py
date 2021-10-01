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
    with open("setup.py", "w", encoding="utf-8") as setup_py:
        setup_py.write("from setuptools import setup")
        setup_py.write("setup(")
        setup_py.write("\tname=\"{}\",".format(name))
        setup_py.write("\tversion=\"1.0\",")
        setup_py.write("\tdescription=\"\",")
        setup_py.write("\tkeywords=\"\",")
        setup_py.write("\tauthor=\"\",")
        setup_py.write("\tpackages=[\"{}\"],".format(name))
        setup_py.write("\tentry_points={\"console_scripts\": [\"\"]},")
        setup_py.write("\tinclude_package_data=True,")
        setup_py.write("\tzip_safe=False")
        setup_py.write("\t)")


def create(lang: str, program: str, prname: str) -> None:
    """Create everything."""
    makedir(lang, program, prname)
