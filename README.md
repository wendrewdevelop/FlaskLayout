# Flask base layout projects
Blog app

## Install requirements

*install this in your virtualenv*
__$ pip install -e .__

*You can observe that the project is now installed with pip list.*
__$ pip list__

Package        Version   Location
-------------- --------- ----------------------------------
click          6.7
Flask          1.0
flaskr         1.0.0     /home/user/Projects/yourprojectfoldername
itsdangerous   0.24
Jinja2         2.10
MarkupSafe     1.0
pip            9.0.3
setuptools     39.0.1
Werkzeug       0.14.1
wheel          0.30.0

## Running system in Development

*Install requirements*
$ pip install requirements-dev.txt

*Set global envs*
__For Linux and Mac:__
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development

__For Windows cmd, use set instead of export:__
$ set FLASK_APP=flaskr
$ set FLASK_ENV=development

__For Windows PowerShell, use $env: instead of export:__
$ $env:FLASK_APP = "flaskr"
$ $env:FLASK_ENV = "development"

*Database configuration*
$ flask init-db

*Running application*
$ flask run


## Running system in Production

*Install wheel*
$ pip install wheel

*Build your project*
$ python setup.py bdist_wheel

*Run this to define your App*
$ export FLASK_APP=App
$ flask init-db

*Configure the Secret Key*
*Use this command*
$ python -c 'import os; print(os.urandom(16))'

*create config.py in instance folder and paste this*
SECRET_KEY = your_generated_secret_key

*Running system instal waitress*
$ pip install waitress

*Initialize server*
$ waitress-serve --call 'flaskr:create_app'
~Serving on http://0.0.0.0:8080'~

__*INSTALL IN OTHER VIRTUALENV*__
pip install App-1.0.0-py3-none-any.whl

## Tests

**Tests in development...**

## Framework

*Access framework docs*
__https://flask.palletsprojects.com/en/1.1.x/__