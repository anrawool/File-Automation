#!/bin/sh
# Only for execution in Home server
git switch Nexus
git pull Nexus
systemctl restart nginx gunicorn