# Cookiecutter Data Science


## Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

## To start a new project, run:
------------

    cookiecutter https://github.com/kuchedav/cookiecutter_template.git


## pre-conditions to run all make commands



### pypi
create a ~/.pypi file with the credentials for pypi:
```bash
[distutils]
index-servers=
    pypi
    testpypi

[pypi]
repository: https://upload.pypi.org/legacy/
username: <username>
password: <pwd>

[testpypi]
repository: https://test.pypi.org/legacy/
username: <username>
password: <pwd>
```

### dockerhub
register your kubernetes cluster with this credentials.
```bash
kubectl create secret  
    docker-registry 
    myregistrykey
    --docker-server=DUMMY_SERVER 
    --docker-username=DUMMY_USERNAME 
    --docker-password=DUMMY_DOCKER_PASSWORD 
    --docker-email=DUMMY_DOCKER_EMAIL
```
verify the secret has been created
```bash
kubectl get secrets myregistrykey
```
