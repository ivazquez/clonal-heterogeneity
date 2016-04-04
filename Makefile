all: bin/cloneHD

bin/cloneHD:
	cd cloneHD/src && $(MAKE)
	cp cloneHD/build/cloneHD bin/
	cp cloneHD/build/filterHD bin/

.PHONY: clean
clean:
	cd cloneHD/src && make clean
	rm bin/cloneHD bin/filterHD