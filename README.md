# README for cc-django

This is a django template using [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) with following features:

* [pipenv](https://github.com/pypa/pipenv) as Python Development Workflow
* Dockerfile + docker-compose ready
* Use Makefile as helper
* Pacakges
  * Django
  * django-extensions
  * django-environ
  * celery
  * raven
  * psycopg2-binary
  * django-debug-toolbar
  * ipython
  * pytest

## Usage

### Install cookiecutter

Install with pip

`pip install --user cookiecutter`

Mac

`brew install cookiecutter`

ubuntu

`sudo apt-get install cookiecutter`

### Begin Django Project

Run

`cookiecutter https://github.com/daikeren/cc-django`

```bash
project_name [Project Name]: test123    # Project Name
project_slug [test123]:                 # project_slug: The slug of your project
timezone [UTC]:                         # Timezone
```
