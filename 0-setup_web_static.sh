#!/usr/bin/env bash
#comment
apt-get update
apt-get install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "ya saaaalam" >>  /data/web_static/releases/test/index.html
ln -sf   /data/web_static/releases/test/  /data/web_static/current
chown -R ubuntu:ubuntu /data/
v="location /hbnb_static { alias /data/web_static/current/; }"
n="root /var/www/html;"
sed -i "\%^\t$n%a\ \t$v" /etc/nginx/sites-available/default
nginx -t
service nginx restart
