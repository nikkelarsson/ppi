PROG = ppi
DOCS = docs
PREFIX = $(HOME)/.local
MAN_SRC = $(shell pwd)/$(DOCS)/$(PROG).1
MAN_DST = $(PREFIX)/man/man1
PYTHON = python3  # Use: make PYTHON=python3.[8|9|10] if your python3 < python3.8

.PHONY: install
install:
	@echo "Installing $(PROG)..."
	mkdir -p $(MAN_DST)
	$(PYTHON) -m pip uninstall -qq --yes $(PROG)
	$(PYTHON) -m pip install -qq .
	@echo "All successfully installed!"

.PHONY: install-editable
install-editable:
	@echo "Installing $(PROG)..."
	mkdir -p $(MAN_DST)
	$(PYTHON) -m pip uninstall -qq --yes $(PROG)
	$(PYTHON) -m pip install -qq -e .
	@echo "All successfully installed!"

.PHONY: uninstall
uninstall:
	@echo "Uninstalling $(PROG)..."
	$(PYTHON) -m pip uninstall -qq --yes $(PROG)
	@echo "All successfully uninstalled!"

.PHONY: tests
tests:
	@echo "Running tests..."
	$(PYTHON) -m unittest -v

.PHONY: man
man:
	pandoc $(DOCS)/$(PROG).1.md -s -t man -o $(DOCS)/$(PROG).1

.PHONY: build
build:
	@echo "Building distribution packages..."
	@# First, clean. Better than running: make clean; make build
	rm -rf dist/
	@# Builds both wheel and sdist
	$(PYTHON) -m build

.PHONY: clean
clean:
	@echo "Cleaning distribution packages..."
	rm -rf dist/
	rm -rf *.egg-info/
