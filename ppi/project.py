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
    with open("{}/setup.py".format(name), "w", encoding="utf-8") as setup_py:
        setup_py.write("from setuptools import setup\n\n")
        setup_py.write("setup(\n")
        setup_py.write("\tname=\"{}\",\n".format(name))
        setup_py.write("\tversion=\"1.0\",\n")
        setup_py.write("\tdescription=\"\",\n")
        setup_py.write("\tkeywords=\"\",\n")
        setup_py.write("\tauthor=\"\",\n")
        setup_py.write("\tpackages=[\"{}\"],\n".format(name))
        setup_py.write("\tentry_points={\"console_scripts\": [\"\"]},\n")
        setup_py.write("\tinclude_package_data=True,\n")
        setup_py.write("\tzip_safe=False\n")
        setup_py.write("\t)")


def makeinit(name: str) -> None:
    """Create __init__.py file to the sourcecode dir."""
    with open("{}/{}/__init__.py", "w", encoding="utf-8") as initfile:
        initfile.write()  # Just "touch" the file.


def makereadme(name: str) -> None:
    """Create a README -file."""
    pass


def create(lang: str, program: str, prname: str) -> None:
    """Create everything."""
    makedir(lang, program, prname)
    makesetup(prname)
    makeinit(prname)
