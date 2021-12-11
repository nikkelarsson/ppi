% PPI(1) ppi 1.2.0  
% Niklas Larsson  
% September 2021  

# NAME
ppi – Python project initializer.

# SYNOPSIS
**ppi** \[*–i* | *––git–init*\] \[*–q* | *––quiet*\] \<*name*\>\
**ppi** \[*–h* | *––help*\] \
**ppi** \[*–V* | *––version*\]

# DESCRIPTION
Starting a new project can be sometimes a tedious process, as it usually
includes creating many different files. With **ppi** it is stress-free to start
a new Python project. At bare minimum a basic set of files are created inside
the new project. These files include *README*, *setup.py*, and a *directory* for
the sourcecode, named with the same name as the project itself, containing
*\_\_init\_\_.py* and *main.py*, from which *main.py* is populated with a basic
structure, enableing the developer to start literally writing code right away.
To make things even easier, *setup.py*, during the initialization, is also
populated with a basic structure, so that the program can be easily installed
via **pip**. If a developer wants, it is possible to initialize the project as
a git-repo during the initialization, as well.

# OPTIONS
**–q** | **––quiet**
: Don't print anything to stdout.

**–i** | **––git–init**
: Initialize project as git repo.

**–h** | **––help**
: Print this message.

**–V** | **––version**
: Print **ppi** version.
