# About
Starting  a new project can be sometimes a tedious process: you have to create
quite a few files, directories etc. Maybe you develop projects and upload them
to PyPI and wished that you wouldn't have to each and every time write that
setup.py from scratch? Quite possibly you publish your projects to GitHub (or
other places) and wished that you wouldn't have to each and every time try and
remember what was it you put into your .gitignore last time?

Any of this resonated with you? Try and see if you like **ppi**.

# Installation
**PIP INSTALLATION METHOD COMING IN THE FUTURE. UNTIL THAT, USE THE METHODS BELOW.**

**ppi** can be installed using **make**. If you want to do some exploration with
the sourcecode, change it, and test your changes easily without having to
re-install in between, install the **editable** version. Otherwise just install
the **regular** version.

To install the **regular** version, run:
``` bash
make install
```

To install the **editable** version, run:
``` bash
make install-editable
```

To uninstall, run:
``` bash
make uninstall
```

# Requirements
| Requirement  | Note          |
| -----------: | :------------ |
| Python       | 3.8 or higher |
| OS           | MacOS, Linux  |

# Default files
The following summarizes the structure for a imaginary project, 'superman'.

``` bash
superman/
    |——— docs/
         |——— superman.1.md
    |——— superman/
	     |——— __init__.py
	     |——— main.py
    |——— CHANGELOG.md
    |——— README.md
    |——— MANIFEST.in
    |——— Makefile
    |——— setup.py
```

# Examples
Here are some short overviews of what some files contain, in more detail. There
are many files and a lot of content, too many to be enumerated in this list and
too much to be shown, so only few selected are displayed here.

``` python
# main.py
# ppi generates basic things, like a docstring template, some
# dunder names for specifying metadata, and a main function, which
# makes it nice and easy to start working on a project

"""What does this program do? Document it here in this docstring."""

__program__: str = "<program>"
__author__: str = ""
__copyright__: str = ""
__credits__: list = []
__license__: str = ""
__version__: str = ""
__maintainer__: str = ""
__email__: str = ""
__status__: str = ""


def main() -> None:
    """Main function."""
    pass


if __name__ == "__main__":
    main()
```

``` python
# setup.py
# ppi generates a nice and full setup.py, ready for you to fill it
# with all the things you see necessary for your project. This makes
# it really easy to upload the project to PyPI later on. There are too
# many settings to be enumerated in this example, so only some are shown here

from setuptools import setup

def readme() -> str:
    """Long description."""
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


setup(
    # Name of your project. When you publish this
    # package to PyPI, this name will be registered
    # for you
    name="<project>",  # Required

    # Version?
    version="",  # Required

    # What does your project do?
    #description="",  # Optional

    # Longer description, that users will see
    # then they visit your project at PyPI
    #long_description=readme(),  # Optional

    # Denotes that long desctiption is in Markdown;
    # valid values are: text/plain, text/x-rst and text/markdown.
    # Optional if 'long_description' is written in rst,
    # otherwise required (for plain-text and Markdown)
    #long_description_content_type="text/markdown",  # Optional

    # ...and there are many more!
)
```

``` makefile
# Makefile
# ppi generates a Makefile, populating it with many useful targets, that
# will make it easy for you to:
#   - build source distributions,
#   - build man-pages,
#   - upload your project to PyPI

PROG = <project>
DOCS = docs
PREFIX = $(HOME)/.local
MAN_SRC = $(shell pwd)/$(DOCS)/$(PROG).1
MAN_DST = $(PREFIX)/man/man1/
PYTHON = python3

.PHONY: build
build:
	@echo "Building distribution packages..."
	rm -rf dist/
	$(PYTHON) -m build

.PHONY: check
check:
	@command -v twine &>/dev/null || $(PYTHON) -m pip install -qq twine
	@echo "Checking that brief / long descriptions in setup.py are valid..."
	twine check dist/*

.PHONY: upload
upload:
	@command -v twine &>/dev/null || $(PYTHON) -m pip install -qq twine
	@echo "Attempting to upload $(PROG) to PyPI..."
	twine upload dist/*

# ...and many more!
```

# Todo
- [ ] Update man-pages
