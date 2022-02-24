"""Simple utility for starting new Python projects quickly."""

__author__: str = "Niklas Larsson"
__credits__: list = ["Niklas Larsson"]
__program__: str = "ppi"
__version__: str = "1.2.3b2"

import subprocess
import os
import sys

from ppi.constants import EXIT_ERROR
from ppi.constants import EXIT_SUCCESS
from ppi.parsing import ArgParser
from ppi.texts import DescriptionText
from ppi.texts import HelpText
from ppi.texts import SuccessText
from ppi.texts import UsageText
from ppi.writers import ChangeLogWriter
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
    parser: ArgParser = ArgParser(__program__, language)
    parser.parse_args()

    # Text generators
    generator: dict[str, object] = {
        "description": DescriptionText(__version__),
        "usage": UsageText(),
        "help": HelpText(),
        "success": SuccessText(parser.project)
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

    if not parser.args:
        # Make sure to print the messages etc to stderr here
        generator["description"].switch.stream = sys.stderr
        generator["usage"].switch.stream = sys.stderr

        generator["description"].display(__program__, language)
        generator["usage"].display(__program__, language)

        # Reset the stream back to stdout
        generator["description"].switch.stream = sys.stdout
        generator["usage"].switch.stream = sys.stdout

        sys.exit(EXIT_ERROR)

    if parser.help:
        generator["description"].display(__program__, language)
        generator["usage"].display(__program__, language)
        generator["help"].display(__program__, language)
        sys.exit(EXIT_SUCCESS)

    if parser.version:
        generator["description"].display(__program__, language)
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
            generator["success"].display(__program__, language)

        sys.exit(EXIT_SUCCESS)

    if any([parser.git, parser.quiet, parser.annotate]):
        # Make sure to print the messages to stderr here
        generator["description"].switch.stream = sys.stderr
        generator["usage"].switch.stream = sys.stderr

        generator["description"].display(__program__, language)
        generator["usage"].display(__program__, language)

        # Reset the stream back to stdout
        generator["description"].switch.stream = sys.stdout
        generator["usage"].switch.stream = sys.stdout

        sys.exit(EXIT_ERROR)


if __name__ == "__main__":
    main()
