"""Functions etc. that generate the project files."""

import abc
import datetime
import os
import sys

from ppi import constants
from ppi import errors


class Writer:
    """Base class for all the different writer classes."""

    def __init__(self) -> None:
        """Initializes things that all the subclasses use."""
        self.encoding: str = constants.ENCODING


class Extracter(abc.ABC):
    """Base class for all the different extracter classes."""

    @abc.abstractmethod
    def extract(self, path: str) -> str:
        """
        Extracts string from the beginning of the path.

        If, for example, the path is "project/otherfiles", then
        "project" is extracted. If on the other hand the path
        is just a file and not an actual path (e.g. "project"),
        then that is returned.

        Parameters:
            path.... Path from which to extract the string.
        """
        pass


class StringExtracter(Extracter):
    """Extracter for extracting strings."""

    def extract(self, path: str) -> str:
        """
        Extracts string from the beginning of the path.

        If, for example, the path is "project/otherfiles", then
        "project" is extracted. If on the other hand the path
        is just a file and not an actual path (e.g. "project"),
        then that is returned.

        Parameters:
            path.... Path from which to extract the string.
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
            print("", file=f)


class MakefileWriter(Writer):
    """Writer for writing Makefiles."""

    def __init__(self) -> None:
        """Initializes Makefile related things."""
        super().__init__()
        self.extracter: object = StringExtracter()

    def write(self, path: str) -> None:
        """
        Writes a Makefile file.

        Parameters:
            path....... Path where to write.
        """
        with open(f"{path}", "w", encoding=self.encoding) as f:
            # Makefile variables
            print(f"PROG = {self.extracter.extract(path)}", file=f)
            print(f"DOCS = docs", file=f)
            print("PREFIX = $(HOME)/.local", file=f)
            print("MAN_SRC = $(shell pwd)/$(DOCS)/$(PROG).1", file=f)
            print("MAN_DST = $(PREFIX)/man/man1/", file=f)
            print("PYTHON = python3", file=f)
            print("", file=f)

            # Build -target
            print('.PHONY: build', file=f)
            print('build:', file=f)
            print('\t@echo "Building distribution packages..."', file=f)
            print('\trm -rf dist/', file=f)
            print('\t$(PYTHON) -m build', file=f)
            print('', file=f)

            # Check -target
            print('.PHONY: check', file=f)
            print('check:', file=f)
            print('\t@command -v twine &>/dev/null || $(PYTHON) -m pip install -qq twine', file=f)
            print('\t@echo "Checking that brief / long descriptions in setup.py are valid..."', file=f)
            print('\ttwine check dist/*', file=f)
            print('', file=f)

            # Upload -target
            print('.PHONY: upload', file=f)
            print('upload:', file=f)
            print('\t@command -v twine &>/dev/null || $(PYTHON) -m pip install -qq twine', file=f)
            print('\t@echo "Attempting to upload $(PROG) to PyPI..."', file=f)
            print('\ttwine upload dist/*', file=f)
            print('', file=f)

            # Clean -target
            print('.PHONY: clean', file=f)
            print('clean:', file=f)
            print('\t@echo "Cleaning distribution packages..."', file=f)
            print('\trm -rf dist/', file=f)
            print('', file=f)

            # Man -target
            print(".PHONY: man", file=f)
            print("man:", file=f)
            print("\tpandoc $(DOCS)/$(PROG).1.md -s -t man -o $(DOCS)/$(PROG).1", file=f)
            print("", file=f)

            # Install -target
            print('.PHONY: install', file=f)
            print('install:', file=f)
            print('\t@echo "Installing $(PROG)..."', file=f)
            print('\t$(PYTHON) -m pip uninstall -qq --yes $(PROG)', file=f)
            print('\t$(PYTHON) -m pip install -qq .', file=f)
            print('\t@echo "Install successful."', file=f)
            print('', file=f)

            # Install-editable -target
            print('.PHONY: install-editable', file=f)
            print('install-editable:', file=f)
            print('\t@echo "Installing $(PROG)..."', file=f)
            print('\t$(PYTHON) -m pip uninstall -qq --yes $(PROG)', file=f)
            print('\t$(PYTHON) -m pip install -qq -e .', file=f)
            print('\t@echo "Install successful."', file=f)
            print('', file=f)

            # Uninstall -target
            print('.PHONY: uninstall', file=f)
            print('uninstall:', file=f)
            print('\t@echo "Uninstalling $(PROG)..."', file=f)
            print('\t$(PYTHON) -m pip uninstall -qq --yes $(PROG)', file=f)
            print('\t@echo "Uninstall successful."', file=f)
            print('', file=f)

            # Tests -target
            print('.PHONY: tests', file=f)
            print('tests:', file=f)
            print('\t@echo "Running tests..."', file=f)
            print('\t$(PYTHON) -m unittest -v', file=f)


class ManPageWriter(Writer):
    """Writer for writing man-pages."""

    def __init__(self) -> None:
        """Initializes man-page related things."""
        super().__init__()
        self.extracter: object = StringExtracter()
        self.month: str = datetime.datetime.now().strftime("%b")
        self.year: str = datetime.datetime.now().strftime("%Y")

    def write(self, path: str) -> None:
        """
        Writes a man-page file.

        Parameters:
            path....... Path where to write.
        """
        projectname: str = self.extracter.extract(path)
        with open(f"{path}", "w", encoding=self.encoding) as f:
            print(f"% {projectname.upper()}(1) {projectname} 0.0.0  ", file=f)
            print("% Author's name  ", file=f)
            print(f"% {self.month} {self.year}  ", file=f)
            print("", file=f)
            print("# NAME  ", file=f)
            print(f"{projectname} -- Short, one-line description of the program  ", file=f)
            print("", file=f)
            print("# SYNOPSIS  ", file=f)
            print(f"**{projectname}**  ", file=f)
            print("", file=f)
            print("# DESCRIPTION  ", file=f)
            print("Longer, detailed description of the program  ", file=f)
            print("", file=f)
            print("# OPTIONS  ", file=f)
            print("All the options of the program, in the following format:", file=f)
            print("**short-option**, **long-option**", file=f)
            print(": Short description of what the option(s) do", file=f)


class SetupPyWriter(Writer):
    """Writer for writing setup.py."""

    def __init__(self) -> None:
        """Initializes setup.py related things."""
        super().__init__()
        self.extracter: object = StringExtracter()

    def write(self, path: str) -> None:
        """
        Writes a setup.py file.

        Parameters:
            path....... Path where to write.
        """
        projectname: str = self.extracter.extract(path)
        with open(f"{path}", "w", encoding=self.encoding) as f:
            print("from setuptools import setup", file=f)
            print("", file=f)
            print("", file=f)
            print("def readme() -> str:", file=f)
            print("    \"\"\"Long description.\"\"\"", file=f)
            print("    with open(\"README.md\", \"r\", encoding=\"utf-8\") as f:", file=f)
            print("        return f.read()", file=f)
            print("", file=f)
            print("", file=f)
            print("setup(", file=f)
            print("    # Name of your project. When you publish this", file=f)
            print("    # package to PyPI, this name will be registered for you", file=f)
            print(f"    name=\"{projectname}\",  # Required", file=f)
            print("", file=f)
            print("    # Version?", file=f)
            print("    version=\"\",  # Required", file=f)
            print("", file=f)
            print("    # What does your project do?", file=f)
            print("    #description=\"\",  # Optional", file=f)
            print("", file=f)
            print("    # Longer description, that users will see when", file=f)
            print("    # they visit your project at PyPI", file=f)
            print("    #long_description=readme(),  # Optional", file=f)
            print("", file=f)
            print("    # Denotes that long description is in Markdown;", file=f)
            print("    # valid values are: text/plain, text/x-rst, text/markdown.", file=f)
            print("    # Optional if 'long_description' is written in rst, otherwise", file=f)
            print("    # required (for plain-text and Markdown)", file=f)
            print("    #long_description_content_type=\"text/markdown\",  # Optional", file=f)
            print("", file=f)
            print("    # Who owns this project?", file=f)
            print("    #author=\"\",  # Optional", file=f)
            print("", file=f)
            print("    # Project owner's email", file=f)
            print("    #author_email=\"\",  # Optional", file=f)
            print("", file=f)
            print("    # More info at: https://pypi.org/classifiers/", file=f)
            print("    classifiers=[  # Optional", file=f)
            print("        # How mature this project is? Common values are:", file=f)
            print("        #   3 - Alpha", file=f)
            print("        #   4 - Beta", file=f)
            print("        #   5 - Production/Stable", file=f)
            print("        #\"Development Status :: 3 - Alpha\",", file=f)
            print("", file=f)
            print("        # Who your project is intended for?", file=f)
            print("        # More info at: https://pypi.org/classifiers/", file=f)
            print("        #\"Intended Audience :: Developers\",", file=f)
            print("        #\"\",", file=f)
            print("", file=f)
            print("        # License?", file=f)
            print("        # More info at: https://pypi.org/classifiers/", file=f)
            print("        #\"\",", file=f)
            print("", file=f)
            print("        # Python versions? These aren't checked by 'pip install'", file=f)
            print("        # More info at: https://pypi.org/classifiers/", file=f)
            print("        #\"Programming Language :: Python :: 3\",", file=f)
            print("", file=f)
            print("    ],", file=f)
            print("", file=f)
            print("    # What does your project relate to?", file=f)
            print("    #keywords=\"\",  # Optional", file=f)
            print("", file=f)
            print("    # Does your project consist of only one or few python files?", file=f)
            print("    # If that's the case, use this.", file=f)
            print("    #py_modules=[\"\"],  # Required", file=f)
            print("", file=f)
            print("    # Is your project larger than just few files?", file=f)
            print("    # If that's the case, use this instead of 'py_modules'.", file=f)
            print(f"    packages=[\"{projectname}\"],  # Required", file=f)
            print("", file=f)
            print("    # Which Python versions are supported?", file=f)
            print("    # e.g. 'pip install' will check this and refuse to install", file=f)
            print("    # the project if the version doesn't match", file=f)
            print("    #python_requires=\">=3.8\",  # Optional", file=f)
            print("", file=f)
            print("    # Any dependencies?", file=f)
            print("    #install_requires=[],  # Optional", file=f)
            print("", file=f)
            print("    # Need to install, for example, man-pages that your project has?", file=f)
            print(f"    #data_files=[(\"man/man1\", [\"docs/{projectname}.1\"])],  # Optional", file=f)
            print("", file=f)
            print("    # Any executable scripts?", file=f)
            print("    # For example, the following would provide a command", file=f)
            print(f"    # called '{projectname}' which executes the function 'main' from", file=f)
            print(f"    # file 'main' from package '{projectname}', when invoked:", file=f)
            print("    entry_points={  # Optional", file=f)
            print("        \"console_scripts\": [", file=f)
            print(f"            #\"{projectname}={projectname}.main:main\",", file=f)
            print("        ]", file=f)
            print("    },", file=f)
            print("", file=f)
            print("    # More info at: https://setuptools.pypa.io/en/latest/userguide/datafiles.html", file=f)
            print("    include_package_data=True,  # Optional", file=f)
            print("", file=f)
            print("    # More info at: https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html", file=f)
            print("    zip_safe=False,  # Optional", file=f)
            print("", file=f)
            print("    # Additional URLs that are relevant to your project", file=f)
            print("    project_urls={  # Optional", file=f)
            print("        #\"Bug Reports\": \"https://github.com...\",", file=f)
            print("        #\"Source\": \"https://github.com...\"", file=f)
            print("    }", file=f)
            print(")", file=f)


class DunderInitWriter(Writer):
    """Class for writing __init__.py files."""

    def write(self, path: str) -> None:
        """
        Writes __init__.py file.

        Parameters:
            path....... Path where to write.
        """
        with open(f"{path}", "w", encoding=self.encoding) as f:
            print("", file=f)


class ChangeLogWriter(Writer):
    """Class for writing CHANGELOG.md files."""

    def write(self, path: str) -> None:
        """
        Writes a CHANGELOG.md file.

        Parameters:
            path....... Path where to write.
        """
        with open(f"{path}", "w", encoding=self.encoding) as f:
            print("# Changelog", file=f)
            print("", file=f)
            print("## [unreleased](link-to-release) -- month day year", file=f)
            print("### Added", file=f)


class ManifestWriter(Writer):
    """Class for writing MANIFEST.in files."""

    def write(self, path: str) -> None:
        """
        Writes a MANIFEST.in file.

        Parameters:
            path....... Path where to write.
        """
        with open(f"{path}", "w", encoding=self.encoding) as f:
            print("include LICENSE.txt", file=f)
            print("graft docs*/", file=f)
            print("graft tests*/", file=f)


class ReadMeWriter(Writer):
    """Class for writing README.md files."""

    def write(self, path: str) -> None:
        """
        Writes a README.md file.

        Parameters:
            path....... Path where to write.
        """
        with open(f"{path}", "w", encoding=self.encoding) as f:
            print("# About  ", file=f)
            print("", file=f)
            print("# Installation  ", file=f)
            print("", file=f)
            print("# Requirements  ", file=f)
            print("", file=f)


class GitIgnoreWriter(Writer):
    """Writer for writing .gitignore files."""

    def write(self, path: str) -> None:
        """
        Writes .gitignore file.

        Parameters:
            path... Path where to write.
        """
        with open(f"{path}", "w", encoding=self.encoding) as f:
            print("# Compiled Python modules", file=f)
            print("*.pyc", file=f)
            print("", file=f)
            print("# Virtual environment", file=f)
            print("venv/", file=f)
            print("", file=f)
            print("# Setuptools distribution folder", file=f)
            print("dist/", file=f)
            print("", file=f)
            print("# Man-pages", file=f)
            print("docs/*.1", file=f)
            print("", file=f)
            print("# Python egg metadata", file=f)
            print("*.egg-info/", file=f)
            print("*.egg", file=f)
            print("*__pycache__/", file=f)


class MainWriter(Writer):
    """Writer for writing main.py files."""

    def __init__(self) -> None:
        """Initializes main.py related things."""
        super().__init__()
        self.extracter: object = StringExtracter()

    def write(self, path: str) -> None:
        """
        Writes main.py file.

        Parameters:
            path....... Path where to write.
        """
        projectname: str = self.extracter.extract(path)
        with open(f"{path}", "w", encoding=self.encoding) as f:
            print('"""What does this program do? Document it in this docstring."""', file=f)
            print('', file=f)
            print(f'__program__: str = "{projectname}"', file=f)
            print('__author__: str = ""', file=f)
            print('__copyright__: str = ""', file=f)
            print('__credits__: list = []', file=f)
            print('__license__: str = ""', file=f)
            print('__version__: str = ""', file=f)
            print('__maintainer__: str = ""', file=f)
            print('__email__: str = ""', file=f)
            print('__status__: str = ""', file=f)
            print('', file=f)
            print('', file=f)
            print('def main() -> None:', file=f)
            print('    """Main function."""', file=f)
            print('    pass', file=f)
            print('', file=f)
            print('', file=f)
            print('if __name__ == "__main__":', file=f)
            print('    main()', file=f)
