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
	@echo 'PACKAGE_VERSION: ' $(PACKAGE_VERSION)
	@echo 'PACKAGE_VERSION_CLEAN: ' $(PACKAGE_VERSION_CLEAN)

commands:
	@echo '=============================================='
	@echo '=    displaying all functions available      ='
	@echo '=============================================='
	@echo 'test: run tox to fully test package'
	@echo 'publish: publish package to pypi_test server'
	@echo 'publish_prod: publish package to pypi server'
	@echo 'docker_package: docker build the Dockerfile to create the image'
	@echo 'docker_hub_push: push docker image to docker hub'
	@echo '		Make sure to be loged into docker with an access token'

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

package:
	rm -rf dist/*
	$(PYTHON_INTERPRETER) -m build

check_credentials_exist:
	[ -f ~/.pypi ] && echo 'pypi credentials found' || echo '~/.pypi file not found!'

publish: package check_credentials_exist
	twine check dist/*
	twine upload --repository testpypi --config-file ~/.pypi dist/*
	@echo '==============================================='
	@echo 'THIS COMMAND ONLY DEPLOYS TO TEST_PYPI'
	@echo 'To deploy to PYPI use the command publish_prod'

publish_prod: check_credentials_exist test
	twine check dist/*
	twine upload --repository pypi --config-file ~/.pypi dist/*

test:
	tox

docker_package:
	docker build . -t {{ cookiecutter.chart_name }}:$(PACKAGE_VERSION_CLEAN)

docker_hub_push: docker_package
	docker tag {{ cookiecutter.chart_name }}:$(PACKAGE_VERSION_CLEAN) kuchedav/{{ cookiecutter.chart_name }}:$(PACKAGE_VERSION_CLEAN)
	docker push kuchedav/{{ cookiecutter.chart_name }}:$(PACKAGE_VERSION_CLEAN)

helm:
	helm lint ./helm/
	helm install -name {{ cookiecutter.chart_name }} ./helm
