#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = test
PYTHON_INTERPRETER = $(PROJECT_DIR)/env/bin/python

globals:
	@echo '=============================================='
	@echo '=    displaying all global variables         ='
	@echo '=============================================='
	@echo 'PROJECT_DIR: ' $(PROJECT_DIR)
	@echo 'PROJECT_NAME: ' $(PROJECT_NAME)
	@echo 'PYTHON_INTERPRETER: ' $(PYTHON_INTERPRETER)

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
environment:
	python3 -m venv env
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

active:
	source $(PROJECT_DIR)/env/bin/activate

tox:
	tox
