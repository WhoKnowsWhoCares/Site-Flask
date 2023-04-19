## Site-Flask
### Personal site on Flask

## How to install
$ sudo apt update
$ sudo apt install -y python3-pip python3-venv git nginx postgresql-14
$ sudo mkdir /var/www/site-flask
$ sudo git clone https://github.com/whoknowswhocares/site-flask.git /var/www/site-flask
$ sudo chown -R $USER:www-data /var/www/site-flask

$ cd /var/www/site-flask
$ chmod +x install.sh
$ ./install.sh