#!/bin/sh

cd ..
sudo mv File-Automation Automation 
cd Automation
git switch Nexus
git pull
mkdir databases
mkdir media
cd media
mkdir uploads
cd ..
pip install virtualenv
virtualenv Server
source Server/bin/activate
pip install django gunicorn
python3 manage.py makemigrations
python3 manage.py migrate
