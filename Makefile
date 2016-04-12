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
	@echo '    make notebooks	install notebook requirements in a virtual environment'
	@echo '    make cloneHD	compile the cloneHD submodule'
	@echo '    make clean		cleanup all temporary files'

notebooks:
	test -d "$(VIRTUAL_ENV)" || mkdir -p "$(VIRTUAL_ENV)"
	test -x "$(VIRTUAL_ENV)/bin/python" || virtualenv "$(VIRTUAL_ENV)"
	$(ACTIVATE) && pip install -r src/requirements.txt

cloneHD:
	test -d "cloneHD/build" || mkdir -p "cloneHD/build"
	cd cloneHD/src && $(MAKE)
	test -d "build" || mkdir -p "build"
	cp cloneHD/build/cloneHD build/
	cp cloneHD/build/filterHD build/

clean:
	cd cloneHD/src && $(MAKE) clean
	rm build/cloneHD build/filterHD

.PHONY: all default notebooks cloneHD clean