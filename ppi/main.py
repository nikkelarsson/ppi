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
    language: str = os.getenv("LANG")
    parser: object = parsing.ArgParser(__program__, language)
    parser.parse_args()

    # Get what flags were provided
    help_: bool = parser.help
    git: bool = parser.git
    project: str = parser.project
    quiet: bool = parser.quiet
    version: bool = parser.version
    annotate: bool = parser.annotate
    args: bool = parser.args

    # Text generators
    generator: dict = {
        "description": texts.DescriptionText(__version__),
        "usage": texts.UsageText(),
        "help": texts.HelpText(),
        "success": texts.SuccessText(project)
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

    if not args:
        # Make sure to print the messages etc to stderr here
        generator["description"].switch.stream = sys.stderr
        generator["usage"].switch.stream = sys.stderr

        generator["description"].display(__program__, language)
        generator["usage"].display(__program__, language)

        # Reset the stream back to stdout
        generator["description"].switch.stream = sys.stdout
        generator["usage"].switch.stream = sys.stdout

        sys.exit(constants.EXIT_ERROR)

    if help_:
        generator["description"].display(__program__, language)
        generator["usage"].display(__program__, language)
        generator["help"].display(__program__, language)
        sys.exit(constants.EXIT_SUCCESS)

    if version:
        generator["description"].display(__program__, language)
        sys.exit(constants.EXIT_SUCCESS)

    if project:
        # Set up writers to write files in desired way
        if annotate:
            files["setup"].switch.annotations = True
            files["main"].switch.annotations = True

        # Write necessary directories
        files["directory"].write(f"{project}/{project}")
        files["directory"].write(f"{project}/docs")

        # Write files that go to the root of the project
        files["readme"].write(f"{project}/README.md")
        files["changelog"].write(f"{project}/CHANGELOG.md")
        files["manifest"].write(f"{project}/MANIFEST.in")
        files["setup_py"].write(f"{project}/setup.py")
        files["makefile"].write(f"{project}/Makefile")

        # Write man pages
        files["manpage"].write(f"{project}/docs/{project}.1.md")

        # Write rest of the files
        files["init_py"].write(f"{project}/{project}/__init__.py")
        files["main_py"].write(f"{project}/{project}/main.py")
        files["gitignore"].write(f"{project}/.gitignore")

        if git:
            subprocess.run(["git", "init", "--quiet", f"{project}/"])

        if not quiet:
            generator["success"].display(__program__, language)

        sys.exit(constants.EXIT_SUCCESS)

    if any([git, quiet, annotate]):
        # Make sure to print the messages to stderr here
        generator["description"].switch.stream = sys.stderr
        generator["usage"].switch.stream = sys.stderr

        generator["description"].display(__program__, language)
        generator["usage"].display(__program__, language)

        # Reset the stream back to stdout
        generator["description"].switch.stream = sys.stdout
        generator["usage"].switch.stream = sys.stdout

        sys.exit(constants.EXIT_ERROR)


if __name__ == "__main__":
    main()
