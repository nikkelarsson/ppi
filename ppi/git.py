"""
git.py: ppi command to initialize local folder as git repository.
Author: Niklas Larsson
Date: October 5, 2021
"""

import subprocess as sp


def git_init(prname: str) -> None:
    """Initialize new project as git repo."""
    sp.run(["git", "init", "--quiet", "{}/".format(prname)])
