# Team: Floor11
# Project: F11 Calculator
# Authors: xtalaj00, xkovac57
#
# Makefile created by xtalaj00 for F11 Calculator

XLOGIN=xtalaj00_xkovac57
PREREQ="PyQt5" "qtmodern"
R_DIR="__pycache__"

all: prerequisites run
pack: clean
	@cd ..\..\..\.. & tar.exe -c -f $(XLOGIN).zip $(XLOGIN)
clean:
	@for %%d in ($(R_DIR)) do (if exist %%d rmdir /S /Q %%d)
	@cd ..\..\..\.. & if exist $(XLOGIN).zip del $(XLOGIN).zip
	@cd ..\..\.. & if exist doc (rmdir /S /Q doc & mkdir doc) else (mkdir doc)
test:
	@python mathlib_tests.py
doc: clean
	@doxygen
run:
	@python calc_main.py
profile:
	@python -m cProfile profiling.py < 100_num.txt
prerequisites:
	@for %%p in ($(PREREQ)) do (pip install %%p -q)
help:
	@echo Usage:	make
	@echo		make [COMMAND]
	@echo  .
	@echo  You will need Python 3.9.1 or greater, to run this Calculator
	@echo  Doxygen 1.9.1 or greater is required to generate documentation
	@echo  To fetch all the prerequisites (works only with Python!), try "make prerequisites" or just "make" (this starts the Calculator straight away)
	@echo  .
	@echo COMMAND:
	@echo  all		- Starts the calculator (By default)
	@echo  pack		- Zip the project without unnecessary files
	@echo  clean		- Deletes unnecessary files
	@echo  test		- Runs math library tests
	@echo  doc		- Runs documentation generation
	@echo  run		- Starts the calculator (Same as all - without checking prerequisites!)
	@echo  profile	- Runs profiler with sets of numbers
