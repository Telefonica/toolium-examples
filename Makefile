APP				= selenium_python
ROOT			= $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
VIRTUALENV		?= virtualenv

ifeq ($(OS),Windows_NT)
	BIN = Scripts
	PYTHON ?= $(shell which python).exe
	TMP = $(ROOT)/tmp
else
	BIN = bin
	PYTHON ?= $(shell which python2.7)
	# time = $(shell date +'%Y%m%d-%H%M%S')
	TMP = /tmp/$(APP)
endif

VENV_PREFIX = $(TMP)/.venv
VENV = $(VENV_PREFIX)/$(APP)
REQ = requirements.txt

TESTREQ = requirements_dev.txt

TEST_ARGS=--nocapture --with-xunit --xunit-file=$(ROOT)/dist/nosetest.xml

all: default

default:
	@echo
	@echo "Welcome to '$(APP)' software package:"
	@echo
	@echo "usage: make <command>"
	@echo
	@echo "commands:"
	@echo "    clean         - Remove generated files and directories"
	@echo "    venv          - Create and update virtual environments"
	@echo "    test          - Execute selenium tests"
	@echo "    pylint        - Run pylint"
	@echo

init:
	mkdir -p $(ROOT)/dist

venv: $(VENV)

$(VENV): $(REQ) $(TESTREQ)
	mkdir -p $@; \
	export GIT_SSL_NO_VERIFY=true; \
	$(VIRTUALENV) --no-site-packages --distribute -p $(PYTHON) $@; \
	cp pip.conf $(VENV); \
	cp pip.ini $(VENV); \
	$@/$(BIN)/easy_install --upgrade Pillow; \
	$@/$(BIN)/pip install --upgrade -r $(REQ); \
	$@/$(BIN)/pip install --upgrade -r $(TESTREQ); \

test: init venv
	$(VENV)/$(BIN)/nosetests tests $(TEST_ARGS)

pylint: init venv
	$(VENV)/$(BIN)/pylint --rcfile=pylint.rc -f parseable $(APP) | tee dist/pylint.log
	$(VENV)/$(BIN)/pylint --rcfile=pylint.rc -f parseable tests examples | tee dist/pylint.log
	@echo ">>> OK. Pylint reports generated in $(ROOT)/dist"

clean:
	@echo ">>> Cleaning temporal files..."
	rm -rf $(TMP) dist/
	@echo

.PHONY: all clean test
