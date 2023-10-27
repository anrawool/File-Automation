#!/bin/sh

# Currently in Setup
mkdir ../databases/
mkdir ../databases/audio/
mkdir ../databases/videos/
mkdir ../databases/videos/only_videos
mkdir ../logs/
mkdir ../keys/
mkdir ../downloads/
mkdir ../PvtInfo/

python3 setup_details.py

python3 setup_PvtInfo.py

mv ../PvtInfo/github_token_encrypted.txt ../PvtInfo/github_token.txt
mv ../PvtInfo/google_token_encrypted.txt ../PvtInfo/google_token.txt


read -p "Would you like to continue with server setup? [y/n]: " confirmation

if [[ $confirmation =~ ^[Yy]$ ]]; then
    echo "Setting Up Server..."
elif [[ $confirmation =~ ^[Nn]$ ]]; then
    echo "You chose not to continue."
    exit
else
    echo "Invalid choice. Please enter 'Y' for Yes or 'n' for No."
fi

# read -p "Please enter your login username which is used in the server: " username
# Currently in User-Interface


cd ../
main_directory=$(pwd)

cd User-Interface/

# Server virtualenv to be setup beforehand to be activated...

current_directory=$(pwd)
default_port=8022
default_assist="Nexus"
read -p "Which port should the server listen to? (Default is 8022): " port
read -p "What is the name of your home assistant? (Default is Nexus): " assist
port="${port:-$default_port}"
assist="${assist:-$default_assist}"

assistname = "${assist}UI"

chmod +x setup.sh
./setup.sh
# Currently in Setup
cd ../Setup/
deactivate

python3 server_file.py