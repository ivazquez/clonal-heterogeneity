all: notebooks cloneHD
	
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
	@echo '    make notebooks	install the package in a virtual environment'
	@echo '    make cloneHD		recreate the virtual environment'
	@echo '    make clean		cleanup all temporary files'

notebooks:
	test -d "$(VIRTUAL_ENV)" || mkdir -p "$(VIRTUAL_ENV)"
	test -x "$(VIRTUAL_ENV)/bin/python" || virtualenv "$(VIRTUAL_ENV)"
	$(ACTIVATE) && pip install -r src/requirements.txt

cloneHD:
	mkdir -p cloneHD/build
	cd cloneHD/src && $(MAKE)
	mkdir -p build
	cp cloneHD/build/cloneHD build/
	cp cloneHD/build/cloneHD build/
	cp cloneHD/build/filterHD build/

clean:
	cd cloneHD/src && make clean
	rm build/pre-filter build/cloneHD build/filterHD

.PHONY: clean