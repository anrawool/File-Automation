
import os

main_directory = os.path.abspath("../")
username = input("Please enter your login username which is used in the server: ")
assist = input("What would you like to name your home assistant? [Default is Nexus] ")
port = input("What is the port at which the server will run? [Default is 8022]")
if port == '':
    port = 8022
if assist == '':
    assist = 'Nexus'

Gunicorn_Socket = """
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

"""

Gunicorn_Service = f"""
[Service]
User={username}
Group=www-data
WorkingDirectory={main_directory}



ExecStart={main_directory}/Server/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          {assist}.wsgi:application

Restart=always
RestartSec=3
[Install]
WantedBy=multi-user.target
"""

Nginx_Service = """
server {
    listen """ + str(port) + """;
    server_name """ + assist + """home.ai;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root """ + main_directory + """;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
"""

with open("./gunicorn.socket", 'w+') as file:
    file.write(Gunicorn_Socket)

os.system("sudo mv ./gunicorn.socket /etc/systemd/system/gunicorn.socket")

with open("./gunicorn.service", 'w+') as file:
    file.write(Gunicorn_Service)

os.system("sudo mv ./gunicorn.service /etc/systemd/system/gunicorn.service")

os.system("sudo systemctl start gunicorn.socket")
os.system("sudo systemctl enable gunicorn.socket")

with open(f"./{assist}UI", "w+") as file:
    file.write(Nginx_Service)

os.system(f"sudo mv ./{assist}UI /etc/nginx/sites-available/{assist}UI")

os.system(f"sudo ln -s /etc/nginx/sites-available/{assist}UI /etc/nginx/sites-enabled/")
os.system("sudo systemctl restart nginx")
os.system("sudo systemctl restart gunicorn")