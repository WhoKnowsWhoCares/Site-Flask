#!/bin/bash
project_domain=""
db_name=""
user_name=""
user_pass=""
project_path=`pwd`

sudo systemctl start postgresql
sudo systemctl enable postgresql

read -p "Your domain without protocol (for example, google.com): " project_domain
read -p "Your name for database: " db_name
read -p "Your name for database super user: " user_name
read -p "Your pass for database super user: " user_pass

python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install wheel
pip install flask gunicorn
pip install -r requirements.txt

sed -i "s~dbms_template_path~$project_path~g" nginx/site.conf systemd/gunicorn.service
sed -i "s~dbms_template_domain~$project_domain~g" nginx/site.conf src/config/settings.py

sudo ln -s $project_path/nginx/site.conf /etc/nginx/sites-enabled/
sudo ln -s $project_path/systemd/gunicorn.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo service nginx restart

sudo mv .env.template .env
sed -i "s~dbms_template_db_name~$db_name~g" .env .pgpass
sed -i "s~dbms_template_db_user~$user_name~g" .env .pgpass
sed -i "s~dbms_template_db_pass~$user_pass~g" .env .pgpass
sudo -u postgres create user $user_name with password "$user_pass";
sudo -u postgres alter user $user_name superuser;
sudo -u postgres create database $db_name;
sudo -u postgres grant all privileges on database $db_name to $user_name;

flask db init
flask db migrate
flask db upgrade