import os
import sys
import __meta
from Controllers.server_conn import *

connector = SSH_Connection('sarthak')
commands = ['cd Public/Automation', 'git switch Nexus', 'git pull Nexus', 'systemctl restart nginx gunicorn']

for command in commands:
    connector.exec_command(command)
print("Process Completed")