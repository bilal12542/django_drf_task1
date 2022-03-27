# Django_Drf_Test

The project is to demonstrate the understanding of django and rest framework. This project consists of custom user model where a user can sign-up with its email and login to the it's account through their emails. It allows registered user to post article, view, update and delete.

## Features

- Sign-up and login
- view users and edit profile if the user is authorized
- view articles, create, update and delete if the user is authorized

## Installation

Before installing the project, python, pip is required to run the project.

1- Install python3-venv
```
$ apt-get install python3-venv  
```
2- Create a directory
```
$ mkdir djangoenv
```
3- Create virtual environment
```
$ python3 -m venv djangoenv  
```
4- Activate virtual environment
```
$ source djangoenv/bin/activate  
```
5- Clone the project
```
$ git clone <link-of-the-project>
```
6- Install all the dependencies of the project
```
$ pip install -r requirements.txt
```
Lastly, run the code
```
$ python manage.py runserver
```

