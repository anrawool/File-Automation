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
    echo "Invalid choice. Please enter 'y' for Yes or 'n' for No."
fi

read -p "Please enter your login username which is used in the server: " username
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
echo "Opening gunicorn.socket file"
sudo touch /etc/systemd/system/gunicorn.socket
sudo touch /etc/systemd/system/gunicorn.service

sudo cat <<EOF > /etc/systemd/system/gunicorn.socket
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target
EOF

sudo cat <<EOF > /etc/systemd/system/gunicorn.service
[Service]
User=$username
Group=www-data
WorkingDirectory=$current_directory



ExecStart=$main_directory/Server/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          $assistname.wsgi:application

Restart=always
RestartSec=3
[Install]
WantedBy=multi-user.target
EOF

sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo cat <<EOF > /etc/nginx/sites-available/NexusUI
server {
    listen $port;
    server_name ${assist}home.ai;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root $current_directory;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
EOF

sudo ln -s /etc/nginx/sites-available/NexusUI /etc/nginx/sites-enabled/
sudo systemctl restart nginx
sudo systemctl restart gunicorn