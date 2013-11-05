**Notice:** This project is still in the making. The documentation is
incomplete. There's no license yet. I will remove this notice, when I think the
project is ready.

# Django-Angular-Boilerplate

A Boilerplate which sets up a basic starter for a
[Heroku](https://www.heroku.com/) deployable
[Django](http://www.djangoproject.com) application with an
[Angular.js](http://www.angularjs.org) frontend and a
[Django REST Framework](http://django-rest-framework.org/) backed REST API.

## What's inside

Django-Angular-Boilerplate integrates the excellent
[ng-boilerplate](http://joshdmiller.github.io/ng-boilerplate/#/home) project
for its frontend part. The backend part is built on
[Django](http://www.djangoproject.com), Django-REST-Framework and a few utility
apps which make Django development easier.

List of installed Django apps:

* [Django Toolbelt](includes [Django](http://www.djangoproject.com),
  [psycopg2](https://pypi.python.org/pypi/psycopg2),
  [gunicorn](https://pypi.python.org/pypi/gunicorn),
  [dj-database-url](https://github.com/kennethreitz/dj-database-url)
  [dj-static](https://github.com/kennethreitz/dj-static))
* [South](http://south.aeracode.org/)
* [Django extensions](https://github.com/django-extensions/django-extensions)
* [Django-REST-Framework](http://django-rest-framework.org/)

# Prerequisites
For everything to work properly you need to satisfy the following requirements:

* The [PostgreSql](http://www.postgresql.org/download/) database server.
* A version of [Python](http://www.python.org). I recommend using the excellent
  [pyenv](https://github.com/yyuu/pyenv) to install and manage Python
  installations. [Heroku supports Python 2.7.4 or 3.3](https://devcenter.heroku.com/articles/python-runtimes)
* To manage isolated Python environments you will need to utilise
  [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation).
* The [virtualenvwrapper plugin for pyenv](https://github.com/yyuu/pyenv-virtualenvwrapper)
  to use virtualenvwrapper inside your pyenv managed Python.
* A version of [Node.js](http://nodejs.org/). I recommend using
  [Node Version Manager](https://github.com/creationix/nvm) for hassle free
  installation and management of different Node.js versions.
* Getting the source code requires [Git](http://git-scm.com/) version control.

If you have been developing with Python and Node.js already, you are likely to
satisfy most of the requirements anyway.

# Installation

This assumes your system meets all the above prerequisites.

* Create a new virtual python environment `mkvirtualenv <YOUR_ENVIRONEMENT>`
* Configure your PostgreSql database and note down your database name, username
  and password.
* Clone the repository `git clone <URL>`
* Add the following to your `~/virtualenvs/<YOURENVIRONMENT>/bin/postactivate`
  file

```shell
export DEBUG="True"
export DATABASE_URL="postgres://<USERNAME>:<PASSWORD>@<DATABASE_SERVER_NAME>/<DATABASE_NAME>"
```

Example DATABASE_URL: `postgres://john:secret@localhost/django_db`

* Change into your project directory and install pip dependencies:
  `cd <YOU PROJECT DIRECTORY> && pip install -r requirements.txt`
* Setup your database tables and superuser by issueing:
  `python manage.py syncdb`.
* Change into the frontend directory and install dependencies:

```shell
$ cd frontend
$ npm -g install grunt-cli karma bower
$ npm install
$ bower install
```

Done!

## Verify your installation

Open a terminal, go to your `frontend` directory and run `grunt watch`. The
build process should start and finish without errors and the terminal should
show:

```shell
Running "karma:unit" (karma) task

Running "delta" task
Waiting...
```

Open another terminal and go to your project root directory and run
`foreman start`. Which should give you an output like this:

```shell
15:33 $ foreman start
15:34:00 web.1  | started with pid 1170
15:34:00 web.1  | 2013-11-04 15:34:00 [1173] [INFO] Starting gunicorn 18.0
15:34:00 web.1  | 2013-11-04 15:34:00 [1173] [INFO] Listening at: http://0.0.0.0:5000 (1173)
15:34:00 web.1  | 2013-11-04 15:34:00 [1173] [INFO] Using worker: sync
15:34:00 web.1  | 2013-11-04 15:34:00 [1178] [INFO] Booting worker with pid: 1178
```

You can now go to http://0.0.0.0:5000 and view the bootstrapped page.

# Explanations

The Django configuration is based on
[Getting Started with Django on Heroku](https://devcenter.heroku.com/articles/getting-started-with-django).

Your Django dependencies are stored in `requirements.txt`. When you install
additional applications in your virtual Python, make sure to update your
`requirements.txt` with `pip freeze > requirements.txt`.

This configurations assumes Python 2.7.4 because that is the latest non 3.x
version supported by Heroku. If you decide to change to a different Python
version make sure to update your `runtime.txt` accordingly. The contents of
file has no effect on your local development environment whatsoever.

All the real magic happens in three directories, `backend`, `config` and
`frontend`.

* `backend` is a Django app which will be home to your server side specific
  code. The idea is to implement your REST API in this place.
* `config` contains Django's configuration, namely `settings.py`, your URL
  configuration in `urls.py` and your WSGI configuration in `wsgi.py`.
* `frontend` contains your Angular.js application. This basically is a clone of
  [ng-boilerplate](http://joshdmiller.github.io/ng-boilerplate/#/home) and
  contains its own set of README files which you are encouraged to read
  through.

## DEBUG mode

You have to set the `DEBUG="True"` environment variable on your local
development machine as explained in the installation instruction. In
`settings.py` there is a switch which provides different versions of your
Angular.js application depending on whether or not your application is in DEBUG
mode.

When `DEBUG="True"`, Django will serve uncompressed, unconcatenated JavaScript
and CSS files for easier debugging.

When `DEBUG="False"` or if `DEBUG` is not set at all Django will serve the
compiled, compressed, concatenated JavaScript and CSS files for faster page
loading.