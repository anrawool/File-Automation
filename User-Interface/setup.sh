#!/bin/sh

# Currently in User-Interface Folder
cd ../..
# Currently in Parent of File-Automation Folder
sudo mv File-Automation Automation 
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
pip install virtualenv
virtualenv ../Server
source ../Server/bin/activate
pip install django gunicorn
python3 manage.py makemigrations
python3 manage.py migrate
# Check if the font directory exists
if [ ! -d "static/fonts" ]; then
    # If the directory doesn't exist, create it
    mkdir -p "$font_directory"
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