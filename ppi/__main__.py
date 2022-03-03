"""
Generate Python projects easily.

Examples:

$ ppi HelloWorld
-> Generates a project called "HelloWorld" to current working directory

$ ppi --annotate HelloWorld
-> Same as the previous, but generates *.py files with type hints

$ ppi --git-init HelloWorld
-> Generates the "HelloWorld" normally + initializes it as git repo
"""

__author__: str = "Niklas Larsson"
__credits__: list = ["Niklas Larsson"]
__program__: str = "ppi"
__version__: str = "1.2.3b2"

import subprocess
import os
import sys

from ppi.constants import EXIT_ERROR
from ppi.constants import EXIT_SUCCESS
from ppi.parsing import ArgumentParser
from ppi.errors import BadArgumentErrorFinnish  # Error handlers
from ppi.errors import BadArgumentErrorEnglish
from ppi.errors import ExtraArgumentErrorFinnish
from ppi.errors import ExtraArgumentErrorEnglish
from ppi.texts import AdditionalHelpTextFinnish  # Text producers
from ppi.texts import AdditionalHelpTextEnglish
from ppi.texts import DescriptionTextFinnish
from ppi.texts import DescriptionTextEnglish
from ppi.texts import HelpTextFinnish
from ppi.texts import HelpTextEnglish
from ppi.texts import SuccessTextFinnish
from ppi.texts import SuccessTextEnglish
from ppi.texts import UsageTextFinnish
from ppi.texts import UsageTextEnglish
from ppi.writers import ChangeLogWriter  # File writers
from ppi.writers import DirectoryWriter
from ppi.writers import InitPyWriter
from ppi.writers import GitIgnoreWriter
from ppi.writers import MainPyWriter
from ppi.writers import ManifestWriter
from ppi.writers import MakefileWriter
from ppi.writers import ManPageWriter
from ppi.writers import ReadMeWriter
from ppi.writers import SetupPyWriter


def main() -> None:
    language: str = os.environ["LANG"]
    parser: ArgumentParser = ArgumentParser(__program__, language)
    parser.parse_args()

    # Help text producers
    helptxt: dict[str, object] = {
        "fi_FI.UTF-8": HelpTextFinnish(__program__),
        "en_US.UTF-8": HelpTextEnglish(__program__),
    }

    # Additional help text producers
    add_helptxt: dict[str, object] = {
        "fi_FI.UTF-8": AdditionalHelpTextFinnish(__program__),
        "en_US.UTF-8": AdditionalHelpTextEnglish(__program__),
    }

    # Description text producers
    desctxt: dict[str, object] = {
        "fi_FI.UTF-8": DescriptionTextFinnish(__program__, __version__),
        "en_US.UTF-8": DescriptionTextEnglish(__program__, __version__),
    }

    # Usage text producers
    usgtxt: dict[str, object] = {
        "fi_FI.UTF-8": UsageTextFinnish(__program__),
        "en_US.UTF-8": UsageTextEnglish(__program__),
    }

    # Success text producers
    succtxt: dict[str, object] = {
        "fi_FI.UTF-8": SuccessTextFinnish(__program__, parser.project),
        "en_US.UTF-8": SuccessTextEnglish(__program__, parser.project),
    }

    # Text generators
    generator: dict[str, object] = {
        "description": desctxt.get(language, desctxt.get("en_US.UTF-8")),
        "usage": usgtxt.get(language, usgtxt.get("en_US.UTF-8")),
        "help": helptxt.get(language, helptxt.get("en_US.UTF-8")),
        "add_help": add_helptxt.get(language, add_helptxt.get("en_US.UTF-8")),
        "success": succtxt.get(language, succtxt.get("en_US.UTF-8")),
    }

    # File writers
    files: dict[str, object] = {
        "directory": DirectoryWriter(),
        "setup_py": SetupPyWriter(),
        "changelog": ChangeLogWriter(),
        "manifest": ManifestWriter(),
        "gitignore": GitIgnoreWriter(),
        "makefile": MakefileWriter(),
        "readme": ReadMeWriter(),
        "main_py": MainPyWriter(),
        "init_py": InitPyWriter(),
        "manpage": ManPageWriter(),
    }

    # Invalid argument error -handlers
    invarg_error: dict[str, object] = {
        "fi_FI.UTF-8": BadArgumentErrorFinnish(parser.invargs),
        "en_US.UTF-8": BadArgumentErrorEnglish(parser.invargs),
    }

    # Extra argument error -handlers
    xarg_error: dict[str, object] = {
        "fi_FI.UTF-8": ExtraArgumentErrorFinnish(parser.xargs),
        "en_US.UTF-8": ExtraArgumentErrorEnglish(parser.xargs),
    }

    # Error message generators
    error: dict[str, object] = {
        "invarg": invarg_error.get(language, invarg_error.get("en_US.UTF-8")),
        "xarg": xarg_error.get(language, xarg_error.get("en_US.UTF-8")),
    }

    if parser.invargs:
        generator["description"].switch.stream = sys.stderr
        generator["usage"].switch.stream = sys.stderr
        generator["add_help"].switch.stream = sys.stderr

        generator["description"].display()
        generator["usage"].display()
        error["invarg"].throw()
        generator["add_help"].display()

        generator["description"].switch.stream = sys.stdout
        generator["usage"].switch.stream = sys.stdout
        generator["add_help"].switch.stream = sys.stdout

        sys.exit(EXIT_ERROR)

    if parser.xargs:
        generator["description"].switch.stream = sys.stderr
        generator["usage"].switch.stream = sys.stderr
        generator["add_help"].switch.stream = sys.stderr

        generator["description"].display()
        generator["usage"].display()
        error["xarg"].throw()
        generator["add_help"].display()

        generator["description"].switch.stream = sys.stdout
        generator["usage"].switch.stream = sys.stdout
        generator["add_help"].switch.stream = sys.stdout

        sys.exit(EXIT_ERROR)

    if not parser.args:
        # Make sure to print the messages etc to stderr here
        generator["description"].switch.stream = sys.stderr
        generator["usage"].switch.stream = sys.stderr
        generator["add_help"].switch.stream = sys.stderr

        generator["description"].display()
        generator["usage"].display()
        generator["add_help"].display()

        # Reset the stream back to stdout
        generator["description"].switch.stream = sys.stdout
        generator["usage"].switch.stream = sys.stdout
        generator["add_help"].switch.stream = sys.stdout

        sys.exit(EXIT_ERROR)

    if parser.help:
        generator["description"].display()
        generator["usage"].display()
        generator["help"].display()
        sys.exit(EXIT_SUCCESS)

    if parser.version:
        generator["description"].display()
        sys.exit(EXIT_SUCCESS)

    if parser.project:
        if parser.annotate: # Set up writers to write files in desired way
            files["setup_py"].switch.annotations = True
            files["main_py"].switch.annotations = True

        # Write necessary directories
        files["directory"].write(f"{parser.project}/{parser.project}")
        files["directory"].write(f"{parser.project}/docs")

        # Write files that go to the root of the project
        files["readme"].write(f"{parser.project}/README.md")
        files["changelog"].write(f"{parser.project}/CHANGELOG.md")
        files["manifest"].write(f"{parser.project}/MANIFEST.in")
        files["setup_py"].write(f"{parser.project}/setup.py")
        files["makefile"].write(f"{parser.project}/Makefile")

        # Write man pages
        files["manpage"].write(f"{parser.project}/docs/{parser.project}.1.md")

        # Write rest of the files
        files["init_py"].write(f"{parser.project}/{parser.project}/__init__.py")
        files["main_py"].write(f"{parser.project}/{parser.project}/main.py")
        files["gitignore"].write(f"{parser.project}/.gitignore")

        if parser.git:
            subprocess.run(["git", "init", "--quiet", f"{parser.project}/"])

        if not parser.quiet:
            generator["success"].display()

        sys.exit(EXIT_SUCCESS)

    if any([parser.git, parser.quiet, parser.annotate]):
        # Make sure to print the messages to stderr here
        generator["description"].switch.stream = sys.stderr
        generator["usage"].switch.stream = sys.stderr
        generator["add_help"].switch.stream = sys.stderr

        generator["description"].display()
        generator["usage"].display()
        generator["add_help"].display()

        # Reset the stream back to stdout
        generator["description"].switch.stream = sys.stdout
        generator["usage"].switch.stream = sys.stdout
        generator["add_help"].switch.stream = sys.stdout

        sys.exit(EXIT_ERROR)


if __name__ == "__main__":
    main()
