#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PYTHON_INTERPRETER = $(PROJECT_DIR)/env/bin/python
PACKAGE_VERSION_CLEAN = $(shell uv --version)


globals:
	@echo '=============================================='
	@echo '=    displaying all global variables         ='
	@echo '=============================================='
	@echo 'PROJECT_DIR: ' $(PROJECT_DIR)
	@echo 'PYTHON_INTERPRETER: ' $(PYTHON_INTERPRETER)
	@echo 'PACKAGE_VERSION_CLEAN: ' $(PACKAGE_VERSION_CLEAN)

commands:
	@echo '=============================================='
	@echo '=    displaying all functions available      ='
	@echo '=============================================='
	@echo 'test: run tox to fully test package'
	@echo 'package: build the package using uv'
	@echo 'publish: publish the package using uv'
	@echo 'docker_package: docker build the Dockerfile to create the image'
	@echo 'docker_hub_push: push docker image to docker hub'
	@echo '		Make sure to be loged into docker with an access token'
	@echo 'helm: build docker package, upload to docker hub, delete local image...'
	@echo '		...delete current helm install and install new helm chart'

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

package:
	@echo 'Building package using uv'
	python -m uv build

publish:
	@echo 'Publishing package using uv'
	python -m uv publish

test:
	tox

git:
	git add .
	git commit -m "debug"
	git push origin main

docker_package:
	@echo '==========================================================================='
	@echo 'MAKE SURE TO RUN ONLY ON A CLEAN GIT BRANCH'
	@echo '==========================================================================='
	docker build . -t kuchedav/{{ cookiecutter.chart_name }}:$(PACKAGE_VERSION_CLEAN)

docker_hub_push: docker_package
	docker push kuchedav/{{ cookiecutter.chart_name }}:$(PACKAGE_VERSION_CLEAN)

docker_clean:
	docker rmi kuchedav/{{ cookiecutter.chart_name }}:$(PACKAGE_VERSION_CLEAN)

helm: docker_hub_push docker_clean
	sed -i "" "/^\([[:space:]]*version: \).*/s//\1$(PACKAGE_VERSION_CLEAN)/" helm/Chart.yaml
	helm lint ./helm/
	helm uninstall {{ cookiecutter.chart_name }}
	helm install {{ cookiecutter.chart_name }} ./helm
