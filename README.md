# About
Starting  a new project can be sometimes a tedious process, as it usually
includes manually creating many different files -- and a good bunch of
these files are usually the same regardless of the project.

With **ppi**, it is stress-free to start a new Python project.  At bare minimum,
a [basic set of files](#default-files) are  created inside the  new project,
automating lot of the manual labour. By automating project creation like this,
**ppi** saves us a lot of time and enables us to start writing code right away.
To make things even better, **ppi** makes it possible to initialize new project
as a local git-repo, and, in addition to that, even create a remote-repo to GitHub,
for example, automating that same old task as well!

# Installation
**ppi** can be installed using **make**. If you want to do some exploration with
the sourcecode and change it and test your changes easily without having to
**make install** after each change, you can install the **editable** version of
**ppi**. Otherwise, you can install the **regular** version. To start off, go to
the root of the project and run either of the following:

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

# Default files
As mentioned in the beginning, a set of files are created when creating a new
project.  From these files, setup.py, during the initialization, is populated
with some basic parameters, so that the program can be installed with **pip**.
In addition, main.py is populated with a basic skeleton-structure, providing a
good starting point.

The structure for new projects looks like the following:

``` bash
project-root/
    |——— README
	|——— setup.py
    |——— sourcecode/
		    |——— __init__.py
			|——— main.py
```
