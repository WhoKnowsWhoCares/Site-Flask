## Site-Flask
### Site on Flask mainly for personal usage.


## How to install
On the host install dependencies and clone repo
```
$ sudo apt update
$ sudo apt install -y python3-pip python3-venv git nginx postgresql-14
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
> Now change file .env, .pgpass


## Use poetry as package manager
$ curl -sSL https://install.python-poetry.org | python3 -
$ echo 'export PATH="$HOME/.local/bin:$PATH' >> ~/zshrc"
$ poetry config virtualenvs.in-project true
$ poetry install
$ poetry shell

## Database management
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
