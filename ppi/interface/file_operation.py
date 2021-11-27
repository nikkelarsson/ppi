"""
file_operation.py: Project file creation.
Author: Niklas Larsson
Date: September 30, 2021
"""


import datetime as dt
import os
import sys

from ppi.interface import errors
from ppi.static import exit_codes


ENC: str = "utf-8"


class ManPages:
    """Class that handles the creation of man-pages."""
    def __init__(self) -> None:
        self.month: str = dt.datetime.now().strftime("%b")
        self.year: str = dt.datetime.now().strftime("%Y")

    def makedocsdir(self, projectname: str) -> None:
        """Create dir for docs like man-pages."""
        os.makedirs("{0}/docs".format(projectname), exist_ok=True)

    def makemanpages(self, projectname: str) -> None:
        """Create basic man-pages skeleton."""
        with open("{0}/docs/{0}.1.md".format(projectname), "w", encoding=ENC) as manp:
            manp.write("% {0}(1) {1} 0.1\n".format(projectname.upper(), projectname))
            manp.write("% Author's name here\n")
            manp.write("% {0} {1}\n\n".format(self.month, self.year))
            manp.write("# NAME\n")
            manp.write("{0} -- Short description of the program.\n\n".format(projectname))
            manp.write("# SYNOPSIS\n")
            manp.write("**{0}** \[*OPT\_SHORT* | *OPT\_LONG*\]\n\n".format(projectname))
            manp.write("# DESCRIPTION\n")
            manp.write("More detailed description of the program.\n\n")
            manp.write("# OPTIONS\n")
            manp.write("**OPT\_SHORT** | **OPT\_LONG**\n")
            manp.write(": Description about flag(s).\n")


class Makefile:
    """Makefile related operations."""
    def create(self, project: str) -> None:
        """Create a Makefile."""
        with open("{}/Makefile".format(project), "w", encoding=ENC) as mf:
            # Makefile variables
            mf.write(f"PROGRAM = {project}\n")
            mf.write(f"MAN_PAGES_SRC = $(shell pwd)/docs/$(PROGRAM).1\n")
            mf.write("MAN_PAGES_DST = /usr/local/man/man1/\n")
            mf.write("PYTHON = python3\n")
            mf.write("\n")

            # Install -target
            mf.write(".PHONY: install\n")
            mf.write("\t@echo \"Installing $(PROGAM) ...\"\n")
            mf.write("\t$(PYTHON) -m pip install -qq .\n")
            mf.write("\t@echo \"Installing man pages ...\"\n")
            mf.write("\tmkdir -p $(MAN_PAGES_DST)\n")
            mf.write("\tcp -f $(MAN_PAGES_SRC) $(MAN_PAGES_DST)\n")
            mf.write("\t@echo \"Install successful.\"\n")
            mf.write("\n")

            # Install-editable -target
            mf.write(".PHONY: install-editable\n")
            mf.write("\t@echo \"Installing $(PROGAM) ...\"\n")
            mf.write("\t$(PYTHON) -m pip install -qq -e .\n")
            mf.write("\t@echo \"Installing man pages ...\"\n")
            mf.write("\tmkdir -p $(MAN_PAGES_DST)\n")
            mf.write("\tcp -f $(MAN_PAGES_SRC) $(MAN_PAGES_DST)\n")
            mf.write("\t@echo \"Install successful.\"\n")
            mf.write("\n")

            # Uninstall -target
            mf.write(".PHONY: uninstall\n")
            mf.write("\t@echo \"Uninstalling $(PROGAM) ...\"\n")
            mf.write("\t$(PYTHON) -m pip uninstall -qq --yes $(PROGRAM)\n")
            mf.write("\t@echo \"Uninstalling man pages ...\"\n")
            mf.write("\trm -f $(MAN_PAGES_DST)$(PROGRAM).1\n")
            mf.write("\t@echo \"Everything uninstalled.\"\n")
            mf.write("\n")

            # Tests -target
            mf.write(".PHONY: tests\n")
            mf.write("\t@echo \"Running tests ...\"\n")
            mf.write("\t$(PYTHON) -m unittest -v")


def makedir(lang: str, program: str, name: str) -> None:
    """Create dirs for a project and it's sourcecode."""
    if os.path.exists(name):
        errors.direxistserror(lang, program, name)
        sys.exit(exit_codes.ERROR)
    os.makedirs("{0}/{0}".format(name), exist_ok=True)


def makesetup(name: str) -> None:
    """Create setup.py -file."""
    with open("{}/setup.py".format(name), "w", encoding=ENC) as setup_py:
        script: str = "{0}={0}.main:main".format(name)
        setup_py.write("from setuptools import setup\n\n")
        setup_py.write("setup(\n")
        setup_py.write("    name=\"{}\",\n".format(name))
        setup_py.write("    version=\"1.0\",\n")
        setup_py.write("    description=\"\",\n")
        setup_py.write("    keywords=\"\",\n")
        setup_py.write("    author=\"\",\n")
        setup_py.write("    packages=[\"{}\"],\n".format(name))
        setup_py.write("    entry_points={\"console_scripts\": [\"%s\"]},\n" % script)
        setup_py.write("    include_package_data=True,\n")
        setup_py.write("    zip_safe=False\n")
        setup_py.write(")")


def makeinit(name: str) -> None:
    """Create __init__.py file to the sourcecode dir."""
    with open("{0}/{0}/__init__.py".format(name), "w", encoding=ENC) as initfile:
        initfile.write("")  # Just "touch" the file.


def makereadme(name: str) -> None:
    """Create a README -file."""
    with open("{}/README.md".format(name), "w", encoding=ENC) as readme:
        readme.write("# About\n")
        readme.write("Something about the program ...\n\n")

        readme.write("# Installation\n")
        readme.write("Instructions on how to install the program etc.\n")
        readme.write("Below you can specify the installation methods.\n\n")

        readme.write("``` bash\n")
        readme.write("\n")
        readme.write("```\n\n")


def makemain(name: str) -> None:
    """Create main.py -file."""
    with open("{0}/{0}/main.py".format(name), "w", encoding=ENC) as main:
        main.write("\"\"\"\n")
        main.write("main.py\n")
        main.write("Author:\n")
        main.write("Date:\n")
        main.write("\"\"\"\n")
        main.write("\n\n")
        main.write("def main() -> None:\n")
        main.write("    pass\n")
        main.write("\n\n")
        main.write("if __name__ == \"__main__\":\n")
        main.write("    pass\n")


def create(lang: str, program: str, prname: str) -> None:
    """Create everything."""
    manpage_h: object = ManPages()  # Man-page handler.

    makedir(lang, program, prname)

    # Stuff to create inside the "root" dir.
    manpage_h.makedocsdir(prname)
    manpage_h.makemanpages(prname)
    makereadme(prname)
    makesetup(prname)

    # Stuff to create inside the "sourcecode" dir.
    makeinit(prname)
    makemain(prname)
