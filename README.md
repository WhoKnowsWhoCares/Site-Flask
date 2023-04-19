## Site-Flask
### Personal site on Flask

## How to install
$ sudo apt update
$ sudo apt install -y python3-pip python3-venv git nginx postgresql-14
$ sudo mkdir /var/www/site-flask
$ sudo git clone https://github.com/whoknowswhocares/site-flask.git /var/www/site-flask
$ sudo chown -R $USER:www-data /var/www/site-flask


$ sudo mv .env.template .env
> Change file .env

$ cd /var/www/site-flask
$ chmod +x install.sh
$ ./install.sh

## Database management
$ sudo systemctl start postgresql
$ sudo systemctl enable postgresql
$ sudo passwd postgres
$ su - postgres
$ export PATH=$PATH:/usr/lib/postgresql/14/bin
$ createdb --encoding UNICODE site_db --username postgres
$ exit

$ sudo -u postgres psql
$ create user <user> with password <password>;
$ grant all privileges on database site_db to <user>;
$ \q

flask db migrate
flask db upgrade
