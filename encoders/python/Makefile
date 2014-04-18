
#####################
# tamper for python #
#####################

all: package

build: deps
	@echo "Building Tamper for Python..."
	@-python setup.py build

test: build
	@echo "Running testsuite..."
	@-nosetests --verbose --with-coverage --cover-package=tamper --cover-branches

install: package
	@echo "Installing Tamper for Python..."
	@-python setup.py install

package: build
	@echo "Building Tamper release packages..."
	@-bin/python setup.py sdist bdist_egg bdist_dumb

deps: .Python

clean:
	@echo "Cleaning py{c,o}'s..."
	@-find . -name "*.py[c,o]" -exec rm -f {} \;

	@echo "Cleaning build/ and dist/..."
	@-rm -fr build/ dist/

envclean:
	@echo "Cleaning virtual environment..."
	@-rm -fr .Python lib include man

distclean: clean envclean
	@echo "Resetting codebase..."
	@-git clean -xdf
	@-git reset --hard


## == environment == ##
.Python:
	@echo "Setting up virtual environment..."
	@-virtualenv .
