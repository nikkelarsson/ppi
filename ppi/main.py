"""Simple utility for starting new Python projects quickly."""

import subprocess
import os
import sys

from ppi import constants
from ppi import texts
from ppi import files
from ppi import parsing


__author__: str = "Niklas Larsson"
__credits__: list = ["Niklas Larsson"]
__version__: str = "1.2.1"
__program__: str = "ppi"

args: bool
git: bool
help_: bool
language: str = os.getenv("LANG")
project: str = None
quiet: bool
version: bool


def main(argv: list=sys.argv, argc: int=len(sys.argv)) -> None:
    parser: object = parsing.ArgParser(argv, __program__, __version__, language)
    parser.parse_args()

    # Get what flags were provided
    help_ = parser.help_requested
    git = parser.git_init_requested
    project = parser.project
    quiet = parser.quiet_requested
    version = parser.version_requested

    args = argc >= 2
    if not args:
        texts.DescriptionText(
            __version__,
            stream=sys.stderr
        ).display(__program__, language)

        texts.UsageText(
            __version__,
            stream=sys.stderr
        ).display(__program__, language)
        sys.exit(constants.EXIT_ERROR)

    if help_:
        texts.DescriptionText(__version__).display(__program__, language)
        texts.UsageText(__version__).display(__program__, language)
        texts.HelpText().display(__program__, language)
        sys.exit(constants.EXIT_SUCCESS)

    if version:
        texts.DescriptionText(__version__).display(__program__, language)
        sys.exit(constants.EXIT_SUCCESS)

    if project:
        # Write necessary directories
        files.DirectoryWriter().write(f"{project}/{project}")
        files.DirectoryWriter().write(f"{project}/docs")

        # Write files that go to the root of the project
        files.ReadmeWriter().write(f"{project}/README.md")
        files.ChangelogWriter().write(f"{project}/CHANGELOG.md")
        files.ManifestWriter().write(f"{project}/MANIFEST.in")
        files.SetupPyWriter().write(f"{project}/setup.py")
        files.MakefileWriter().write(f"{project}/Makefile")

        # Write man pages
        files.ManPageWriter().write(f"{project}/docs/{project}.1.md")

        # Write rest of the files
        files.DunderInitWriter().write(f"{project}/{project}/__init__.py")
        files.MainWriter().write(f"{project}/{project}/main.py")

        if git:
            subprocess.run(["git", "init", "--quiet", f"{project}/"])
            files.GitIgnoreWriter().write(f"{project}/.gitignore")

        if not quiet:
            texts.SuccessText(project).display(__program__, language)

        sys.exit(constants.EXIT_SUCCESS)

    if any([git, quiet]):
        texts.DescriptionText(
            __version__,
            stream=sys.stderr
        ).display(__program__, language)

        texts.UsageText(
            __version__,
            stream=sys.stderr
        ).display(__program__, language)

        sys.exit(constants.EXIT_ERROR)


if __name__ == "__main__":
    main()
