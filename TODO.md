# To Do

## Features / changes / updates / improvements etc. to the current ones
- [x] Implement "-h" and "--help" -flags.
- [x] Implement "-V" and "--version" -flags.
- [x] Implement functionality that would make **ppi** create man-pages, as well.
- [x] Make the success message bold etc.
- [ ] Implement a feature that would enable **ppi** to create a Makefile during
  the initialization.
- [ ] Utilize Github's / Gitea's API (or both).
- [ ] Implement a feature that would enable creating CHANGELOG file.
- [ ] Generate version in format X.X.X in setup.py, instead of the current X.X
- [ ] When generating main.py, write version there too
- [ ] When generating main.py, write __author__, __licence__, __version__,
  __program__, __author_email__ etc. there
- [ ] When generating main.py, write the "if __name__" block in such way that it
  calls the main() straight away (I don't realize why I haven't done this yet)
- [ ] When generating any file, always write empty line at the end (PEP8 standard)
- [ ] When generating the "main" script or file of the program, generate a
  hashbang line at the top of that file
- [ ] When generating man pages, write AUTHOR section there
- [ ] When generating man pages, write more "simple" synopsis under the SYNOPSIS
  section
- [ ] When generating man pages, don't write the author name at the top of the
  file (author's name could be given on the command line, instead. This would
  however require that feature to be implemented first)
- [ ] When generating man pages, don't end the NAME section's description with a
  period
- [ ] If initializing project as git git -repo, create .gitignore to the root

## Refactoring
- [x] Update docs
- [ ] Reformat all the module docstrings -> only show module description in the
  docstring
- [ ] Reformat all modules: leave an empty line at the end of each file (PEP8)

## Other stuff
- [x] Add CHANGELOG
- [ ] Attach a licence
