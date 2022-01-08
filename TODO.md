# To Do

## Features / changes / updates / improvements etc. to the current ones
### NOTE: these todos are sorted from "more important" to "less important"
- [ ] Put **ppi** to the PyPI. The name **ppi** is actually taken there already,
  so the name needs to be changed to something else. (Maybe create a fork off of
  **ppi** as the "new" project and come up with a name that's not already
  reserved, I don't know...)

- [x] When writing setup.py, write the following there (in addition):
  - [x] A function that returns README's contents to long_description
  - [x] long_description - An empty string can be written (user can fill it manually)
  - [x] long_description_content_type - Can be "text/markdown"
  - [x] author_email - An empty string can be written (user can fill it manually)
  - [x] classifiers - Should be a list. (User can fill it manually)
  - [x] py_modules - Can be left empty (user can fill it manually, if needed)
  - [x] python_requires - Can be left as an empty string (user can fill it, if needed)
  - [x] install_requires - Can be left as an empty list (user can fill it, if needed)
  - [x] data_files - It should be a list and look like [(dir, [file1, file2])],
    where 'dir' is where to install the additional files 'file1' and 'file2'
  - [x] project_urls - It should be a dict and contain perhaps the following fields:
    - [x] "Source": "url/to/project"
    - [x] "Bug Reports": "url/to/project/issues"

- [x] If initializing project as a git -repo, create .gitignore to the root of
  the project. Check the following link (scroll to the bottom of the page) for
  what to write there: https://python-packaging.readthedocs.io/en/latest/everything.html

- [x] Implement a feature that would enable **ppi** to create a Makefile during
  the initialization. The following targets could be written to the Makefile:
  - [x] build - for building sdists and wheels
  - [x] clean - for deleting/cleaning the sdists etc. (build target could do this also?)
  - [x] man - for generating man pages using **pandoc**

- [x] Implement a feature so that **ppi** generates a CHANGELOG file

- [x] When generating main.py, write __author__, __licence__, __version__,
  __program__, __author_email__ etc. there

- [x] When generating main.py, write the "if __name__" block in such way that it
  calls the main() straight away (I don't realize why I haven't done this yet)

- [ ] When generating man pages, write more "simple" synopsis under the SYNOPSIS
  section

- [ ] When generating man pages, don't write the author name at the top of the
  file (author's name could be given on the command line, instead. This would
  however require that feature to be implemented first)

- [ ] When generating man pages, don't end the NAME section's description with a
  period

- [ ] Utilize Github's / Gitea's API (or both)

- [ ] When generating man pages, write AUTHOR section there (this is actually
  done already by **pandoc**. However, if the man-pages ought to be created
  without using **pandoc**, then this would be relevant)

## Refactoring

## Other stuff
- [ ] Attach a licence
