[![Tests](https://github.com/WhoKnowsWhoCares/Site-Flask/actions/workflows/build-test.yml/badge.svg?branch=master)](https://github.com/WhoKnowsWhoCares/Site-Flask/actions/workflows/build-test.yml) [![Docker Build](https://github.com/WhoKnowsWhoCares/Site-Flask/actions/workflows/docker-build-publish.yml/badge.svg?branch=master)](https://github.com/WhoKnowsWhoCares/Site-Flask/actions/workflows/docker-build-publish.yml) [![Deploy by Runner](https://github.com/WhoKnowsWhoCares/Site-Flask/actions/workflows/registry-pull.yml/badge.svg?branch=master)](https://github.com/WhoKnowsWhoCares/Site-Flask/actions/workflows/registry-pull.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Site-Flask

This site on Flask mainly for personal usage, but it could be used as template for other sites on flask.
In the description you could find how to use it.

- There are supported two ways for run site (classic and in docker).
- Also exist functions for privacy based on users credentials.
- Tests examples if you will need it later.
- Connected to the telegram bot to send some events from site.

## How to install and run

There are two ways to install - classic and docker

#### Classic installation

Here we install nginx, database such as postgres or mysql, then run shell script to create python environment with additional pakages from requirement.txt and configure gunicorn and nginx in systemd.

```
$ sudo apt update
$ sudo apt install -y python3-pip python3-venv git nginx postgresql-14 mysql-server
$ sudo mkdir /var/www/site-flask
$ sudo git clone https://github.com/whoknowswhocares/site-flask.git /var/www/site-flask
$ sudo chown -R $USER:www-data /var/www/site-flask
```

Run script to create python environment and configure nginx and gunicorn

```
$ cd /var/www/site-flask
$ chmod +x install.sh
$ ./install.sh
```

Now change file .env, .pgpass and restart nginx

#### Docker installation

This is an easyer way - you just build docker and run it through docker-compose.

I'm using my private docker repository and usualy just pull docker insted of building it from source. If you want to build, make sure that in docker-compose.yaml there is uncommented part:

```
build:
    context: .
    dockerfile: Dockerfile
```

To run docker compose use:

```
$ docker volume create site_flask_data
$ docker compose up -d
```

#### Create default user

As default I don't allow to create new users on the site, but have all for it.
To create single default user from .env variables there is cli command to use in flask, to run it:

> if you are using docker, get into shell by running
> $ docker exec -it <container_id> bash

```
$ flask create_user
```

## Use poetry as package manager

```
$ curl -sSL https://install.python-poetry.org | python3 -
$ echo 'export PATH="$HOME/.local/bin:$PATH' >> ~/zshrc"
$ poetry config virtualenvs.in-project true
$ poetry install
$ poetry shell
```

## Database management (just in case)

On production mode use postgres

```
$ sudo systemctl start postgresql
$ sudo systemctl enable postgresql
$ sudo passwd postgres
```

Create site_db database

```
$ su - postgres
$ export PATH=$PATH:/usr/lib/postgresql/14/bin
$ createdb --encoding UNICODE site_db --username postgres
$ exit
```

Create user for our database

```
$ sudo -u postgres psql
$ create user <user> with password <password>;
$ grant all privileges on database site_db to <user>;
$ \q
```

```
flask db migrate
flask db upgrade
```
