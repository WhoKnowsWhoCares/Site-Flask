## Site-Flask
### Personal site on Flask

## How to install
$ sudo apt update
$ sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools \
    python3-venv git nginx postgresql postgresql-contrib
$ sudo mkdir /var/www/site-flask
$ git clone git@github.com:whoknowswhocares/site-flask.git /var/www/site-flask
$ sudo chown -R www:www-data /var/www/site-flask

$ cd /var/www/site-flask
$ ./install.sh