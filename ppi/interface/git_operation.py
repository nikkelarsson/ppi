"""Git -specific routines etc."""


import subprocess as sp


def git_init(prname: str) -> None:
    """Initialize new project as git repo."""
    sp.run(["git", "init", "--quiet", "{}/".format(prname)])
