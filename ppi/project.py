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
    with open("{0}/{0}/__init__.py".format(name), "w", encoding="utf-8") as initfile:
        initfile.write("")  # Just "touch" the file.


def makereadme(name: str) -> None:
    """Create a README -file."""
    with open("{}/README.md".format(name), "w", encoding="utf-8") as readme:
        readme.write("# {}\n".format(name))


def makemain(name: str) -> None:
    """Create main.py -file."""
    with open("{0}/{0}/main.py".format(name), "w", encoding="utf-8") as main:
        main.write("\"\"\"\n")
        main.write("main.py\n")
        main.write("Author:\n")
        main.write("Date:\n")
        main.write("\"\"\"\n")
        main.write("\n\n")
        main.write("def main() -> None:\n")
        main.write("\tpass\n")
        main.write("\n\n")
        main.write("if __name__ == \"__main__\":\n")
        main.write("\tpass\n")


def create(lang: str, program: str, prname: str) -> None:
    """Create everything."""
    makedir(lang, program, prname)

    # Stuff to create inside the "root" dir.
    makereadme(prname)
    makesetup(prname)

    # Stuff to create inside the "sourcecode" dir.
    makeinit(prname)
    makemain(prname)
