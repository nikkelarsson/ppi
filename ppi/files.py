"""Functions etc. that generate the project files."""

import abc
import datetime
import os
import sys

from ppi import errors
from ppi import constants


class Writer(abc.ABC):
    """Base class for all the different writer classes."""

    def __init__(self) -> None:
        """Initial values."""
        self.encoding: str = constants.ENCODING

    @abc.abstractmethod
    def write(self, path: str) -> None:
        """
        Prototype function for subclasses.

        Parameters:
            path....... Path where to write the file.
            The path should contain the filename at the end,
            i.e. like "path/to/file.md", for example.
        """
        pass

    def extract_projectname(self, path: str) -> str:
        """
        Extracts projectname from the beginning of the path.

        If, for example, the path is "project/otherfiles", then
        "project" is extracted. If on the other hand the path
        is just a file and not an actual path (e.g. "project"),
        then that is returned.

        Parameters:
            path.... Path from which to extract the projectname.
        """
        return path.split("/")[0]


class DirectoryWriter(Writer):
    """Writer for writing directories."""

    def write(self, path: str) -> None:
        """
        Writes a directory or multiple ones.

        Parameters:
            path.... Path where to write the directory/directories.
        """
        os.makedirs(path, exist_ok=True)


# NOTE: This class is not ready to use!
class EmptyFileWriter(Writer):
    """Generic writer for writing empty files."""

    def write(self, path: str) -> None:
        """
        Writes any kind of file.

        Parameters:
            path....... Path where to write.
        """
        with open(f"{path}", "w", encoding=self.encoding) as f:
            f.write("")


class MakefileWriter(Writer):
    """Writer for writing Makefiles."""

    def write(self, path: str) -> None:
        """
        Writes a Makefile.

        Parameters:
            path....... Path where to write.
        """
        with open(f"{path}", "w", encoding=self.encoding) as f:
            # Makefile variables
            f.write(f"PROG = {super().extract_projectname(path)}\n")
            f.write(f"DOCS = docs\n")
            f.write("PREFIX = $(HOME)/.local\n")
            f.write("MAN_SRC = $(shell pwd)/$(DOCS)/$(PROG).1\n")
            f.write("MAN_DST = $(PREFIX)/man/man1/\n")
            f.write("PYTHON = python3\n")
            f.write("\n")

            # Build -target
            f.write(".PHONY: build\n")
            f.write("build:\n")
            f.write("\t@echo \"Building distribution packages...\"\n")
            f.write("\trm -rf dist/\n")
            f.write("\t$(PYTHON) -m build\n")
            f.write("\n")

            # Clean -target
            f.write(".PHONY: clean\n")
            f.write("clean:\n")
            f.write("\t@echo \"Cleaning distribution packages...\"\n")
            f.write("\trm -rf dist/\n")
            f.write("\n")

            # Man -target
            f.write(".PHONY: man\n")
            f.write("man:\n")
            f.write("\tpandoc $(DOCS)/$(PROG).1.md -s -t man -o $(DOCS)/$(PROG).1\n")
            f.write("\n")

            # Install -target
            f.write(".PHONY: install\n")
            f.write("\t@echo \"Installing $(PROG)...\"\n")
            f.write("\t$(PYTHON) -m pip uninstall -qq --yes $(PROG)\n")
            f.write("\t$(PYTHON) -m pip install -qq .\n")
            f.write("\t@echo \"Install successful.\"\n")
            f.write("\n")

            # Install-editable -target
            f.write(".PHONY: install-editable\n")
            f.write("\t@echo \"Installing $(PROG)...\"\n")
            f.write("\t$(PYTHON) -m pip uninstall -qq --yes $(PROG)\n")
            f.write("\t$(PYTHON) -m pip install -qq -e .\n")
            f.write("\t@echo \"Install successful.\"\n")
            f.write("\n")

            # Uninstall -target
            f.write(".PHONY: uninstall\n")
            f.write("\t@echo \"Uninstalling $(PROG)...\"\n")
            f.write("\t$(PYTHON) -m pip uninstall -qq --yes $(PROG)\n")
            f.write("\t@echo \"Uninstall successful.\"\n")
            f.write("\n")

            # Tests -target
            f.write(".PHONY: tests\n")
            f.write("\t@echo \"Running tests...\"\n")
            f.write("\t$(PYTHON) -m unittest -v")


class ManPageWriter(Writer):
    """Writer for writing man-pages."""

    def __init__(self) -> None:
        """Initial values."""
        super().__init__()
        self.month: str = datetime.datetime.now().strftime("%b")
        self.year: str = datetime.datetime.now().strftime("%Y")

    def write(self, path: str) -> None:
        """
        Writes a man-page file.

        Parameters:
            path....... Path where to write.
        """
        projectname: str = super().extract_projectname(path)
        with open(f"{path}", "w", encoding=self.encoding) as f:
            f.write(f"% {projectname.upper()}(1) {projectname} 0.1  \n")
            f.write("% Author's name  \n")
            f.write(f"% {self.month} {self.year}  \n")
            f.write("\n")
            f.write("# NAME  \n")
            f.write(f"{projectname} -- Short, one-line description of the program  \n")
            f.write("\n")
            f.write("# SYNOPSIS  \n")
            f.write(f"**{projectname}**  \n")
            f.write("\n")
            f.write("# DESCRIPTION  \n")
            f.write("Longer, detailed description of the program  \n")
            f.write("\n")
            f.write("# OPTIONS  \n")
            f.write("All the options of the program, in the following format:\n")
            f.write("**short-option**, **long-option**\n")
            f.write(": Short description of what the option(s) do\n")


class SetupPyWriter(Writer):
    """Writer for writing setup.py."""

    def write(self, path: str) -> None:
        """
        Writes a setup.py file.

        Parameters:
            path....... Path where to write.
        """
        projectname: str = self.extract_projectname(path)
        with open(f"{path}", "w", encoding=self.encoding) as f:
            f.write("from setuptools import setup\n")
            f.write("\n")
            f.write("\n")
            f.write("def readme() -> str:\n")
            f.write("    \"\"\"Long description.\"\"\"\n")
            f.write("    with open(\"README.md\", \"r\", encoding=\"utf-8\") as f:\n")
            f.write("    return f.read()\n")
            f.write("\n")
            f.write("\n")
            f.write("setup(\n")
            f.write("    # Name of your project. When you publish this\n")
            f.write("    # package to PyPI, this name will be registered for you\n")
            f.write(f"    name=\"{projectname}\",  # Required\n")
            f.write("\n")
            f.write("    # Version?\n")
            f.write("    version=\"0.0.1\",  # Required\n")
            f.write("\n")
            f.write("    # What does your project do?\n")
            f.write("    #description=\"\",  # Optional\n")
            f.write("\n")
            f.write("    # Longer description, that users will see when\n")
            f.write("    # they visit your project at PyPI\n")
            f.write("    #long_description=readme(),  # Optional\n")
            f.write("\n")
            f.write("    # Denotes that long description is in Markdown;\n")
            f.write("    # valid values are: text/plain, text/x-rst, text/markdown.\n")
            f.write("    # Optional if 'long_description' is written in rst, otherwise\n")
            f.write("    # required (for plain-text and Markdown)\n")
            f.write("    #long_description_content_type=\"text/markdown\",  # Optional\n")
            f.write("\n")
            f.write("    # Who owns this project?\n")
            f.write("    #author=\"\",  # Optional\n")
            f.write("\n")
            f.write("    # Project owner's email\n")
            f.write("    #author_email=\"\",  # Optional\n")
            f.write("\n")
            f.write("    # More info at: https://pypi.org/classifiers/\n")
            f.write("    classifiers=[  # Optional\n")
            f.write("        # How mature this project is? Common values are:\n")
            f.write("        #   3 - Alpha\n")
            f.write("        #   4 - Beta\n")
            f.write("        #   5 - Production/Stable\n")
            f.write("        #\"Development Status :: 3 - Alpha\",\n")
            f.write("\n")
            f.write("        # Who your project is intended for?\n")
            f.write("        # More info at: https://pypi.org/classifiers/\n")
            f.write("        #\"Intended Audience :: Developers\",\n")
            f.write("        #\"\",\n")
            f.write("\n")
            f.write("        # License?\n")
            f.write("        # More info at: https://pypi.org/classifiers/\n")
            f.write("        #\"\",\n")
            f.write("\n")
            f.write("        # Python versions? These aren't checked by 'pip install'\n")
            f.write("        # More info at: https://pypi.org/classifiers/\n")
            f.write("        #\"Programming Language :: Python :: 3\",\n")
            f.write("\n")
            f.write("    ],\n")
            f.write("\n")
            f.write("    # What does your project relate to?\n")
            f.write("    #keywords=\"\",  # Optional\n")
            f.write("\n")
            f.write("    # Does your project consist of only one or few python files?\n")
            f.write("    # If that's the case, use this.\n")
            f.write("    #py_modules=[\"\"],  # Required\n")
            f.write("\n")
            f.write("    # Is your project larger than just few files?\n")
            f.write("    # If that's the case, use this instead of 'py_modules'.\n")
            f.write(f"    packages=[\"{projectname}\"],  # Required\n")
            f.write("\n")
            f.write("    # Which Python versions are supported?\n")
            f.write("    # e.g. 'pip install' will check this and refuse to install\n")
            f.write("    # the project if the version doesn't match\n")
            f.write("    #python_requires=\">=3.8\",  # Optional\n")
            f.write("\n")
            f.write("    # Any dependencies?\n")
            f.write("    #install_requires=[],  # Optional\n")
            f.write("\n")
            f.write("    # Need to install, for example, man-pages that your project has?\n")
            f.write("    #data_files=[(\"man/man1\", [\"docs/manpage.1\"])],  # Optional\n")
            f.write("\n")
            f.write("    # Any executable scripts?\n")
            f.write("    # For example, the following would provide a command\n")
            f.write(f"    # called '{projectname}' which executes the function 'main' from\n")
            f.write(f"    # file 'main' from package '{projectname}', when invoked:\n")
            f.write("    entry_points={  # Optional\n")
            f.write("        \"console_scripts\": [\n")
            f.write(f"            #\"{projectname}={projectname}.main:main\",\n")
            f.write("        ]\n")
            f.write("    },\n")
            f.write("\n")
            f.write("    # More info at: https://setuptools.pypa.io/en/latest/userguide/datafiles.html\n")
            f.write("    include_package_data=True,  # Optional\n")
            f.write("\n")
            f.write("    # More info at: https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html\n")
            f.write("    zip_safe=False,  # Optional\n")
            f.write("\n")
            f.write("    # Additional URLs that are relevant to your project\n")
            f.write("    project_urls={  # Optional\n")
            f.write("        #\"Bug Reports\": \"https://github.com...\",\n")
            f.write("        #\"Source\": \"https://github.com...\"\n")
            f.write("    }\n")
            f.write(")\n")


class DunderInitWriter(Writer):
    """Class for writing __init__.py files."""

    def write(self, path: str) -> None:
        """
        Writes __init__.py file.

        Parameters:
            path....... Path where to write.
        """
        with open(f"{path}", "w", encoding=self.encoding) as f:
            f.write("")


class ChangelogWriter(Writer):
    """Class for writing CHANGELOG.md files."""

    def write(self, path: str) -> None:
        """
        Writes a CHANGELOG.md file.

        Parameters:
            path....... Path where to write.
        """
        with open(f"{path}", "w", encoding=self.encoding) as f:
            f.write("# Changelog\n")
            f.write("\n")
            f.write("## [unreleased](link-to-release) -- month day year\n")
            f.write("### Added\n")


class ManifestWriter(Writer):
    """Class for writing MANIFEST.in files."""

    def write(self, path: str) -> None:
        """
        Writes a MANIFEST.in file.

        Parameters:
            path....... Path where to write.
        """
        with open(f"{path}", "w", encoding=self.encoding) as f:
            f.write("include LICENCE.txt\n")
            f.write("graft docs*/\n")
            f.write("graft tests*/\n")


class ReadmeWriter(Writer):
    """Class for writing README.md files."""

    def write(self, path: str) -> None:
        """
        Writes a README.md file.

        Parameters:
            path....... Path where to write.
        """
        with open(f"{path}", "w", encoding=self.encoding) as f:
            f.write("# About  \n")
            f.write("\n")
            f.write("# Installation  \n")
            f.write("\n")
            f.write("# Requirements  \n")
            f.write("\n")


class GitIgnoreWriter(Writer):
    """Writer for writing .gitignore files."""

    def write(self, path: str) -> None:
        """
        Writes .gitignore file.

        Parameters:
            path... Path where to write.
        """
        with open(f"{path}", "w", encoding=self.encoding) as f:
            f.write("# Compiled Python modules\n")
            f.write("*.pyc\n")
            f.write("\n")
            f.write("# Virtual environment\n")
            f.write("venv/\n")
            f.write("\n")
            f.write("# Setuptools distribution folder\n")
            f.write("dist/\n")
            f.write("\n")
            f.write("# Python egg metadata\n")
            f.write("*.egg-info/\n")
            f.write("*.egg\n")
            f.write("*__pycache__/\n")


class MainWriter(Writer):
    """Writer for writing main.py files."""

    def write(self, path: str) -> None:
        """
        Writes main.py file.

        Parameters:
            path....... Path where to write.
        """
        projectname: str = self.extract_projectname(path)
        with open(f"{path}", "w", encoding=self.encoding) as f:
            f.write("\"\"\"Short description of what this program does\"\"\"\n")
            f.write("\n")
            f.write("\n")
            f.write(f"__program__: str = \"{projectname}\"\n")
            f.write("__author__: str = \"\"\n")
            f.write("__copyright__: str = \"\"\n")
            f.write("__credits__: list = []\n")
            f.write("__license__: str = \"\"\n")
            f.write("__version__: str = \"\"\n")
            f.write("__maintainer__: str = \"\"\n")
            f.write("__email__: str = \"\"\n")
            f.write("__status__: str = \"\"\n")
            f.write("\n")
            f.write("\n")
            f.write("def main() -> None:\n")
            f.write("    pass\n")
            f.write("\n")
            f.write("\n")
            f.write("if __name__ == \"__main__\":\n")
            f.write("    main()\n")
