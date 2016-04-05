all: install submodule
	
# The following defaults are based on my preferences, but possible for others
# to override thanks to the `?=' operator.
WORKON_HOME ?= $(HOME)/.virtualenvs
VIRTUAL_ENV ?= $(WORKON_HOME)/popdyn
ACTIVATE = . "$(VIRTUAL_ENV)/bin/activate"
	
default:
	@echo "Makefile for the repository"
	@echo
	@echo 'Commands:'
	@echo
	@echo '    make install    install the package in a virtual environment'
	@echo '    make submodule  recreate the virtual environment'
	@echo '    make clean      cleanup all temporary files'

install:
	test -d "$(VIRTUAL_ENV)" || mkdir -p "$(VIRTUAL_ENV)"
	test -x "$(VIRTUAL_ENV)/bin/python" || virtualenv "$(VIRTUAL_ENV)"
	$(ACTIVATE) && pip install -r src/requirements.txt

submodule:
	cd cloneHD/src && $(MAKE)
	cp cloneHD/build/cloneHD bin/
	cp cloneHD/build/filterHD bin/

clean:
	cd cloneHD/src && make clean
	rm bin/cloneHD bin/filterHD

.PHONY: clean