PROGRAM = ppi
MAN_PAGES = ppi.1
MAN_PAGES_SRC = $(shell pwd)/docs/$(MAN_PAGES)
MAN_PAGES_INSTALL = /usr/local/man/man1/
PYTHON_INTERPRETER = python3.8

.PHONY: ppi
ppi:
	@echo "TO INSTALL: sudo make install"
	@echo "TO INSTALL EDITABLE: sudo make install-editable"
	@echo "TO UNINSTALL: sudo make uninstall"

.PHONY: install
install:
	@echo "Installing $(PROGRAM) ..."
	$(PYTHON_INTERPRETER) -m pip install -qq .
	@echo "Installing man -pages ..."
	@mkdir -p $(MAN_PAGES_INSTALL)
	cp -f $(MAN_PAGES_SRC) $(MAN_PAGES_INSTALL)
	@echo "All successfully installed!"

.PHONY: install-editable
install-editable:
	@echo "Installing $(PROGRAM) ..."
	$(PYTHON_INTERPRETER) -m pip install -qq -e .
	@echo "Installing man -pages ..."
	@mkdir -p $(MAN_PAGES_INSTALL)
	cp -f $(MAN_PAGES_SRC) $(MAN_PAGES_INSTALL)
	@echo "All successfully installed!"

.PHONY: uninstall
uninstall:
	@echo "Uninstalling $(PROGRAM) ..."
	$(PYTHON_INTERPRETER) -m pip uninstall -qq --yes $(PROGRAM)
	@echo "Uninstalling man -pages ..."
	rm -f $(MAN_PAGES_INSTALL)$(MAN_PAGES)
	@echo "All successfully uninstalled!"

.PHONY: tests
tests:
	@echo "Running tests ..."
	$(PYTHON_INTERPRETER) -m unittest -v
