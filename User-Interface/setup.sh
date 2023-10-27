#!/bin/sh

# Currently in User-Interface Folder
cd ../..
# Currently in Parent of File-Automation Folder
echo "Installing nginx, gunicorn, vim, virtualenv, ufw and pip"
sudo apt-get install vim
sudo apt-get install ufw
sudo ufw status
sudo ufw enable
sudo ufw allow 22
sudo ufw allow 8022
sudo ufw status
sudo apt install python3-pip python3-dev nginx
sudo pip install virtualenv
sudo mv File-Automation Automation 
echo "File-Automation Folder Renamed"
cd Automation
# Currently in Automation Folder
git switch Nexus
git pull
cd User-Interface
# Currently in User-Interface Folder
mkdir databases
mkdir media
mkdir media/profile_pics
mkdir media/uploads
pip install django gunicorn
pip install -r ../requirements.txt
python manage.py makemigrations
python manage.py migrate

# Check if the font directory exists
if [ ! -d "static/fonts" ]; then
    # If the directory doesn't exist, create it
    mkdir static/fonts 
    echo "Font directory created."
else
    echo "Font directory already exists."
fi
echo "Going ahead with setup"
cd static/fonts/
# Currently in Static/Fonts Folder
mkdir Poppins
cd Poppins
# Currently in Static/Fonts/Poppins Folder
wget -O poppins.zip "https://fonts.google.com/download?family=Poppins"
unzip poppins.zip
rm -rf poppins.zip
cd ../../../
# Currently in User-Interface Folder
echo "Server Files Ready"