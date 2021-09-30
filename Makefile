.PHONY: ppi install reinstall uninstall
PROGRAM = ppi
MAN_PAGES_SRC = $(shell pwd)/docs/ppi.1
MAN_PAGES_INSTALL = /usr/local/man/man1/
PYTHON_INTERPRETER = python3

ppi:
	@echo "TO INSTALL: sudo make install"
	@echo "TO UNINSTALL: sudo make uninstall"
	@echo "TO REINSTALL: sudo make reinstall"

install:
	@echo "Installing $(PROGRAM) ..."
	$(PYTHON_INTERPRETER) -m pip install .
	@echo "Installing man -pages ..."
	@sudo mkdir -p $(MAN_PAGES_INSTALL)
	sudo cp -f $(MAN_PAGES) $(MAN_PAGES_INSTALL)
	sudo gmandb
	@echo "All successfully installed!"

reinstall:
	@echo "Re-installing $(PROGRAM) ..."
	$(PYTHON_INTERPRETER) -m pip install .
	@echo "Re-installing man -pages ..."
	sudo cp -f $(MAN_PAGES) /usr/local/man/man1
	sudo gmandb
	@echo "All successfully re-installed!"

uninstall:
	@echo "Uninstalling $(PROGRAM) ..."
	$(PYTHON_INTERPRETER) -m pip uninstall --yes $(PROGRAM)
	@echo "Uninstalling man -pages ..."
	sudo rm -f /usr/local/man/man1/ppi.1
	@echo "All successfully uninstalled!"
