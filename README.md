**Notice:** This project is still in the making. The documentation is
incomplete. There's no license yet. I will remove this notice, when I think the
project is ready.

# Django-Angular-Boilerplate

A Boilerplate which sets up a basic starter for a
[Heroku](https://www.heroku.com/) deployable
[Django](http://www.djangoproject.com) application with an
[Angular.js](http://www.angularjs.org) frontend and a
[Django REST Framework](http://django-rest-framework.org/) backed REST API.

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