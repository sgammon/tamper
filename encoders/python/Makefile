
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


## == environment == ##
.Python:
	@echo "Setting up virtual environment..."
	@-virtualenv .
