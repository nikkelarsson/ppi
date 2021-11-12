PROGRAM = ppi
MAN_PAGES = ppi.1
MAN_PAGES_SRC = $(shell pwd)/docs/$(MAN_PAGES)
MAN_PAGES_INSTALL = /usr/local/man/man1/
PYTHON_INTERPRETER = python3

ppi:
	@echo "TO INSTALL: sudo make install"
	@echo "TO UNINSTALL: sudo make uninstall"
	@echo "TO REINSTALL: sudo make reinstall"

.PHONY: install
install:
	@echo "Installing $(PROGRAM) ..."
	$(PYTHON_INTERPRETER) -m pip install -qq .
	@echo "Installing man -pages ..."
	@sudo mkdir -p $(MAN_PAGES_INSTALL)
	sudo cp -f $(MAN_PAGES_SRC) $(MAN_PAGES_INSTALL)
	@echo "All successfully installed!"

.PHONY: install-editable
install-editable:
	@echo "Installing $(PROGRAM) ..."
	$(PYTHON_INTERPRETER) -m pip install -qq -e .
	@echo "Installing man -pages ..."
	@sudo mkdir -p $(MAN_PAGES_INSTALL)
	sudo cp -f $(MAN_PAGES_SRC) $(MAN_PAGES_INSTALL)
	@echo "All successfully installed!"

uninstall:
	@echo "Uninstalling $(PROGRAM) ..."
	$(PYTHON_INTERPRETER) -m pip uninstall -qq --yes $(PROGRAM)
	@echo "Uninstalling man -pages ..."
	sudo rm -f $(MAN_PAGES_INSTALL)$(MAN_PAGES) 
	@echo "All successfully uninstalled!"
