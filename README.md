# About
Starting  a new project can be sometimes a tedious process, as it usually
includes manually creating many different files -- and a good bunch of
these files are usually the same regardless of the project.

With **ppi**, it is stress-free to start a new Python project.  At bare minimum,
a [basic set of files](#default-files) are  created inside the  new project,
automating lot of the manual labour. By automating project creation like this,
**ppi** saves us a lot of time and enables us to start writing code right away.

# Installation
**ppi** can be installed using **make**. If you want to do some exploration with
the sourcecode and change it and test your changes easily without having to
**make install** after each change, you can install the **editable** version of
**ppi**. Otherwise, you can install the **regular** version.

To install the **regular** version, run:
``` bash
sudo make install
```

To install the **editable** version, run:
``` bash
sudo make install-editable
```

To uninstall, run:
``` bash
sudo make uninstall
```

# Requirements
| Requirement  | Note          |
| -----------: | :------------ |
| Python       | 3.8 or higher |
| OS           | MacOS, Linux  |

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
