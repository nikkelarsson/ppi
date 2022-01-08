"""Functions etc. that handle creating the files."""


import datetime as dt
import os
import sys
import subprocess as sb

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
            manp.write("% {0}(1) {1} 0.1  \n".format(projectname.upper(), projectname))
            manp.write("% Author's name here  \n")
            manp.write("% {0} {1}  \n\n".format(self.month, self.year))
            manp.write("# NAME  \n")
            manp.write("{0} -- Short description of the program.  \n\n".format(projectname))
            manp.write("# SYNOPSIS  \n")
            manp.write("**{0}** \[*OPT\_SHORT* | *OPT\_LONG*\]  \n\n".format(projectname))
            manp.write("# DESCRIPTION  \n")
            manp.write("More detailed description of the program.  \n\n")
            manp.write("# OPTIONS  \n")
            manp.write("**OPT\_SHORT** | **OPT\_LONG**  \n")
            manp.write(": Description about flag(s).  \n")


class Makefile:
    """Makefile related operations."""

    def create(self, project: str) -> None:
        """Create a Makefile."""
        with open("{}/Makefile".format(project), "w", encoding=ENC) as mf:
            # Makefile variables
            mf.write(f"PROG = {project}\n")
            mf.write(f"DOCS = docs\n")
            mf.write(f"PREFIX = $(HOME)/.local\n")
            mf.write(f"MAN_SRC = $(shell pwd)/$(DOCS)/$(PROG).1\n")
            mf.write("MAN_DST = $(PREFIX)/man/man1/\n")
            mf.write("PYTHON = python3\n")
            mf.write("\n")

            # Build -target
            mf.write(".PHONY: build\n")
            mf.write("build:\n")
            mf.write("\t@echo \"Building distribution packages...\"\n")
            mf.write("\trm -rf dist/\n")
            mf.write("\t$(PYTHON) -m build\n")
            mf.write("\n")

            # Clean -target
            mf.write(".PHONY: clean\n")
            mf.write("clean:\n")
            mf.write("\t@echo \"Cleaning distribution packages...\"\n")
            mf.write("\trm -rf dist/\n")
            mf.write("\n")

            # Man -target
            mf.write(".PHONY: man\n")
            mf.write("man:\n")
            mf.write("\tpandoc $(DOCS)/$(PROG).1.md -s -t man -o $(DOCS)/$(PROG).1\n")
            mf.write("\n")

            # Install -target
            mf.write(".PHONY: install\n")
            mf.write("\t@echo \"Installing $(PROG)...\"\n")
            mf.write("\t$(PYTHON) -m pip uninstall -qq --yes $(PROG)\n")
            mf.write("\t$(PYTHON) -m pip install -qq .\n")
            mf.write("\t@echo \"Install successful.\"\n")
            mf.write("\n")

            # Install-editable -target
            mf.write(".PHONY: install-editable\n")
            mf.write("\t@echo \"Installing $(PROG)...\"\n")
            mf.write("\t$(PYTHON) -m pip uninstall -qq --yes $(PROG)\n")
            mf.write("\t$(PYTHON) -m pip install -qq -e .\n")
            mf.write("\t@echo \"Install successful.\"\n")
            mf.write("\n")

            # Uninstall -target
            mf.write(".PHONY: uninstall\n")
            mf.write("\t@echo \"Uninstalling $(PROG)...\"\n")
            mf.write("\t$(PYTHON) -m pip uninstall -qq --yes $(PROG)\n")
            mf.write("\t@echo \"Uninstall successful.\"\n")
            mf.write("\n")

            # Tests -target
            mf.write(".PHONY: tests\n")
            mf.write("\t@echo \"Running tests...\"\n")
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

        setup_py.write("from setuptools import setup\n")
        setup_py.write("\n")
        setup_py.write("\n")
        setup_py.write("def readme() -> str:\n")
        setup_py.write("    \"\"\"Long description.\"\"\"\n")
        setup_py.write("    with open(\"README.md\", \"r\", encoding=\"utf-8\") as f:\n")
        setup_py.write("    return f.read()\n")
        setup_py.write("\n")
        setup_py.write("\n")
        setup_py.write("setup(\n")
        setup_py.write("    # Name of your project. When you publish this\n")
        setup_py.write("    # package to PyPI, this name will be registered for you\n")
        setup_py.write("    name=\"{}\",  # Required\n".format(name))
        setup_py.write("\n")
        setup_py.write("    # Version?\n")
        setup_py.write("    version=\"0.0.1\",  # Required\n")
        setup_py.write("\n")
        setup_py.write("    # What does your project do?\n")
        setup_py.write("    #description=\"\",  # Optional\n")
        setup_py.write("\n")
        setup_py.write("    # Longer description, that users will see when\n")
        setup_py.write("    # they visit your project at PyPI\n")
        setup_py.write("    #long_description=readme(),  # Optional\n")
        setup_py.write("\n")
        setup_py.write("    # Denotes that long description is in Markdown;\n")
        setup_py.write("    # valid values are: text/plain, text/x-rst, text/markdown.\n")
        setup_py.write("    # Optional if 'long_description' is written in rst, otherwise\n")
        setup_py.write("    # required (for plain-text and Markdown)\n")
        setup_py.write("    #long_description_content_type=\"text/markdown\",  # Optional\n")
        setup_py.write("\n")
        setup_py.write("    # Who owns this project?\n")
        setup_py.write("    #author=\"\",  # Optional\n")
        setup_py.write("\n")
        setup_py.write("    # Project owner's email\n")
        setup_py.write("    #author_email=\"\",  # Optional\n")
        setup_py.write("\n")
        setup_py.write("    # More info at: https://pypi.org/classifiers/\n")
        setup_py.write("    classifiers=[  # Optional\n")
        setup_py.write("        # How mature this project is? Common values are:\n")
        setup_py.write("        #   3 - Alpha\n")
        setup_py.write("        #   4 - Beta\n")
        setup_py.write("        #   5 - Production/Stable\n")
        setup_py.write("        #\"Development Status :: 3 - Alpha\",\n")
        setup_py.write("\n")
        setup_py.write("        # Who your project is intended for?\n")
        setup_py.write("        # More info at: https://pypi.org/classifiers/\n")
        setup_py.write("        #\"Intended Audience :: Developers\",\n")
        setup_py.write("        #\"\",\n")
        setup_py.write("\n")
        setup_py.write("        # License?\n")
        setup_py.write("        # More info at: https://pypi.org/classifiers/\n")
        setup_py.write("        #\"\",\n")
        setup_py.write("\n")
        setup_py.write("        # Python versions? These aren't checked by 'pip install'\n")
        setup_py.write("        # More info at: https://pypi.org/classifiers/\n")
        setup_py.write("        #\"Programming Language :: Python :: 3\",\n")
        setup_py.write("\n")
        setup_py.write("    ],\n")
        setup_py.write("\n")
        setup_py.write("    # What does your project relate to?\n")
        setup_py.write("    #keywords=\"\",  # Optional\n")
        setup_py.write("\n")
        setup_py.write("    # Does your project consist of only one or few python files?\n")
        setup_py.write("    # If that's the case, use this.\n")
        setup_py.write("    #py_modules=[\"\"],  # Required\n")
        setup_py.write("\n")
        setup_py.write("    # Is your project larger than just few files?\n")
        setup_py.write("    # If that's the case, use this instead of 'py_modules'.\n")
        setup_py.write("    packages=[\"{}\"],  # Required\n".format(name))
        setup_py.write("\n")
        setup_py.write("    # Which Python versions are supported?\n")
        setup_py.write("    # e.g. 'pip install' will check this and refuse to install\n")
        setup_py.write("    # the project if the version doesn't match\n")
        setup_py.write("    #python_requires=\">=3.8\",  # Optional\n")
        setup_py.write("\n")
        setup_py.write("    # Any dependencies?\n")
        setup_py.write("    #install_requires=[],  # Optional\n")
        setup_py.write("\n")
        setup_py.write("    # Need to install, for example, man-pages that your project has?\n")
        setup_py.write("    #data_files=[(\"man/man1\", [\"docs/manpage.1\"])],  # Optional\n")
        setup_py.write("\n")
        setup_py.write("    # Any executable scripts?\n")
        setup_py.write("    # For example, the following would provide a command\n")
        setup_py.write("    # called '{}' which executes the function 'main' from\n".format(name))
        setup_py.write("    # file 'main' from package '{}', when invoked:\n".format(name))
        setup_py.write("    entry_points={  # Optional\n")
        setup_py.write("        \"console_scripts\": [\n")
        setup_py.write("            #\"{0}={0}.main:main\",\n".format(name))
        setup_py.write("        ]\n")
        setup_py.write("    },\n")
        setup_py.write("\n")
        setup_py.write("    # More info at: https://setuptools.pypa.io/en/latest/userguide/datafiles.html\n")
        setup_py.write("    include_package_data=True,  # Optional\n")
        setup_py.write("\n")
        setup_py.write("    # More info at: https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html\n")
        setup_py.write("    zip_safe=False,  # Optional\n")
        setup_py.write("\n")
        setup_py.write("    # Additional URLs that are relevant to your project\n")
        setup_py.write("    project_urls={  # Optional\n")
        setup_py.write("        #\"Bug Reports\": \"https://github.com...\",\n")
        setup_py.write("        #\"Source\": \"https://github.com...\"\n")
        setup_py.write("    }\n")
        setup_py.write(")\n")


def makeinit(name: str) -> None:
    """Create __init__.py file to the sourcecode dir."""
    with open("{0}/{0}/__init__.py".format(name), "w", encoding=ENC) as initfile:
        initfile.write("")  # Just "touch" the file.


def makereadme(name: str) -> None:
    """Create a README -file."""
    with open("{}/README.md".format(name), "w", encoding=ENC) as readme:
        readme.write("# About  \n")
        readme.write("Something about the program ...  \n\n")

        readme.write("# Installation  \n")
        readme.write("Instructions on how to install the program etc.  \n")
        readme.write("Below you can specify the installation methods.  \n\n")

        readme.write("``` bash  \n\n")
        readme.write("```  \n")


def makemain(name: str) -> None:
    """Create main.py -file."""
    # Get author's name from git's configuration, if it has been set there.
    _author: str = sb.run(
        ["git", "config", "--get", "user.name"],
        capture_output=True,
        text=True
    ).stdout.replace("\n", "")

    if not _author:
        _author = "<Your name here>"

    with open("{0}/{0}/main.py".format(name), "w", encoding=ENC) as main:
        main.write("\"\"\"\n")
        main.write("main.py\n")
        main.write("Author: {}\n".format(_author))
        main.write("Date: {}\n".format(dt.datetime.now().strftime("%B %-d, %Y")))
        main.write("\"\"\"\n")
        main.write("\n")
        main.write("\n")
        main.write("__author__: str = \"\"\n")
        main.write("__copyright__: str = \"\"\n")
        main.write("__credits__: list = []\n")
        main.write("__license__: str = \"\"\n")
        main.write("__version__: str = \"\"\n")
        main.write("__maintainer__: str = \"\"\n")
        main.write("__email__: str = \"\"\n")
        main.write("__status__: str = \"\"\n")
        main.write("\n")
        main.write("\n")
        main.write("def main() -> None:\n")
        main.write("    pass\n")
        main.write("\n")
        main.write("\n")
        main.write("if __name__ == \"__main__\":\n")
        main.write("    main()\n")


def create(lang: str, program: str, prname: str) -> None:
    """Create everything."""
    manpage_h: object = ManPages()  # Man-page handler.
    makefile_h: object = Makefile()  # Makefile handler

    makedir(lang, program, prname)

    # Stuff to create inside the "root" dir.
    makefile_h.create(prname)
    manpage_h.makedocsdir(prname)
    manpage_h.makemanpages(prname)
    makereadme(prname)
    makesetup(prname)

    # Stuff to create inside the "sourcecode" dir.
    makeinit(prname)
    makemain(prname)
