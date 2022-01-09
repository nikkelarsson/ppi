"""Git-specific routines etc."""


import subprocess


def _mkgitignore(project) -> None:
    """Creates a gitignore file."""
    with open("{}/.gitignore".format(project), "w", encoding="utf-8") as f:
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

def git_init(prname: str) -> None:
    """Initialize new project as git repo."""
    subprocess.run(["git", "init", "--quiet", "{}/".format(prname)])
    _mkgitignore(prname)
