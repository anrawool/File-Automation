#!/bin/sh

pip3 install -r ../requirements.txt
# Currently in User-Interface
cd ../User-Interface/
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
User=sarthak
Group=www-data
WorkingDirectory=/home/sarthak/Public/Automation/User-Interface
ExecStart=/home/sarthak/Public/Automation/Server/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          NexusUI.wsgi:application

Restart=always
RestartSec=3
[Install]
WantedBy=multi-user.target
EOF

sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo cat <<EOF > /etc/nginx/sites-available/NexusUI
server {
    listen 8022;
    server_name www.nexushome.in;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/sarthak/Public/Automation/User-Interface;
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