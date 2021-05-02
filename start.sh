#!/bin/bash
sleep 5
python serverproject/manage.py makemigrations
python serverproject/manage.py migrate
python serverproject/manage.py collectstatic --noinput
uwsgi --socket :8001 --module mysite.wsgi