.PHONY: ppi

MAN_PAGES=$(shell pwd)/docs/ppi.1

ppi:
	@echo "TO INSTALL: sudo make install"
	@echo "TO UNINSTALL: sudo make uninstall"
	@echo "TO REINSTALL: sudo make reinstall"

install:
	echo "Installing ppi ..."
	pip3 install .
	echo "Installing man -pages ..."
	sudo mkdir -p /usr/local/man/man1
	sudo cp $(MAN_PAGES) /usr/local/man/man1
	sudo mandb
	echo "All successfully installed!"

reinstall:
	echo "Re-installing ppi ..."
	pip3 install .
	echo "Re-installing man -pages ..."
	sudo cp $(MAN_PAGES) /usr/local/man/man1
	sudo mandb
	echo "All successfully re-installed!"

uninstall:
	echo "Uninstalling ppi ..."
	pip3 uninstall --yes ppi
	echo "Uninstalling man -pages ..."
	sudo rm /usr/local/man/man1/ppi.1
	echo "All successfully uninstalled!"
