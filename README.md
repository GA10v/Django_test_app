# Django_test_app
Django tutorial 

## Requirements

- Python 3.6+
- pip

## Install

- creates a virtual environment named 'venv':
$ python3 -m venv venv

- activate your brand new virtual environment:
$ source venv/bin/activate

- install Django:
$ pip install Django==2.2

- setup todo app:
$ django-admin startproject todo
$ cd todo
$ django-admin startapp tasks
$ python3 manage.py migrate
$ python3 manage.py createsuperuser

- run app:
$ python3 manage.py runserver