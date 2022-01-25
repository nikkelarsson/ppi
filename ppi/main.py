"""Simple utility for starting new Python projects quickly."""

__author__: str = "Niklas Larsson"
__credits__: list = ["Niklas Larsson"]
__program__: str = "ppi"
__version__: str = "1.2.2b1"

import subprocess
import os
import sys

from ppi import constants
from ppi import parsing
from ppi import texts
from ppi import writers


def main(argc: int=len(sys.argv), argv: list=sys.argv) -> None:
    language: str = os.getenv("LANG")
    parser: object = parsing.ArgParser(argv, __program__, language)
    parser.parse_args()

    # Get what flags were provided
    help_: bool = parser.help
    git: bool = parser.git
    project: str = parser.project
    quiet: bool = parser.quiet
    version: bool = parser.version

    # Text generators
    generator: dict = {
        "description": texts.DescriptionText(__version__),
        "usage": texts.UsageText(),
        "help": texts.HelpText(),
        "success": texts.SuccessText(project)
    }

    # File writers
    files: dict = {
        "directory": writers.DirectoryWriter()
    }

    args = argc >= 2
    if not args:
        generator["description"].display(__program__, language, stream=sys.stderr)
        generator["usage"].display(__program__, language, stream=sys.stderr)
        sys.exit(constants.EXIT_ERROR)

    if help_:
        generator["description"].display(__program__, language, stream=sys.stdout)
        generator["usage"].display(__program__, language, stream=sys.stdout)
        generator["help"].display(__program__, language, stream=sys.stdout)
        sys.exit(constants.EXIT_SUCCESS)

    if version:
        generator["description"].display(__program__, language, stream=sys.stdout)
        sys.exit(constants.EXIT_SUCCESS)

    if project:
        # Write necessary directories
        files["directory"].write(f"{project}/{project}")
        files["directory"].write(f"{project}/docs")

        # Write files that go to the root of the project
        writers.ReadMeWriter().write(f"{project}/README.md")
        writers.ChangeLogWriter().write(f"{project}/CHANGELOG.md")
        writers.ManifestWriter().write(f"{project}/MANIFEST.in")
        writers.SetupPyWriter().write(f"{project}/setup.py")
        writers.MakefileWriter().write(f"{project}/Makefile")

        # Write man pages
        writers.ManPageWriter().write(f"{project}/docs/{project}.1.md")

        # Write rest of the files
        writers.DunderInitWriter().write(f"{project}/{project}/__init__.py")
        writers.MainWriter().write(f"{project}/{project}/main.py")

        if git:
            subprocess.run(["git", "init", "--quiet", f"{project}/"])
            writers.GitIgnoreWriter().write(f"{project}/.gitignore")

        if not quiet:
            generator["success"].display(__program__, language, stream=sys.stdout)

        sys.exit(constants.EXIT_SUCCESS)

    if any([git, quiet]):
        generator["description"].display(__program__, language, stream=sys.stderr)
        generator["usage"].display(__program__, language, stream=sys.stderr)
        sys.exit(constants.EXIT_ERROR)


if __name__ == "__main__":
    main()
