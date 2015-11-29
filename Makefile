PROJECT_DIR=$(shell pwd)
VENV_DIR?=$(PROJECT_DIR)/.env
PIP?=$(VENV_DIR)/bin/pip
PYTHON?=$(VENV_DIR)/bin/python
NOSE?=$(VENV_DIR)/bin/nosetests

.PHONY: all clean test run pip virtualenv

all: virtualenv pip

virtualenv:
	virtualenv -p python3.4 $(VENV_DIR) --no-site-packages

pip: requirements

requirements:
	$(PIP) install -r $(PROJECT_DIR)/requirements.txt

test:
	$(NOSE) $(PROJECT_DIR) --verbose

clean_temp:
	find . -name '*.pyc' -delete
	rm -rf .coverage dist docs/_build htmlcov MANIFEST

clean_venv:
	rm -rf $(VENV_DIR)

clean: clean_temp clean_venv

convert:
	$(PYTHON) converter.py input.txt
	$(info Done.)

