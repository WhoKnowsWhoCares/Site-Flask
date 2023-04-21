#!/bin/bash
project_domain=""
project_path=`pwd`

read -p "Your domain without protocol (for example, google.com): " project_domain

python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install wheel
pip install flask gunicorn
pip install -r requirements.txt

sudo cp .env.template .env
sudo cp .pgpass.template .pgpass
sudo cp nginx/site.conf.template nginx/site.conf
sudo cp systemd/gunicorn.service.template systemd/gunicorn.service

sed -i "s~dbms_template_path~$project_path~g" nginx/site.conf systemd/gunicorn.service
sed -i "s~dbms_template_domain~$project_domain~g" nginx/site.conf

sudo ln -s $project_path/nginx/site.conf /etc/nginx/sites-enabled/
sudo ln -s $project_path/systemd/gunicorn.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl restart nginx
