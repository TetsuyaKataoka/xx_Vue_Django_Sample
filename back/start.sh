#!/bin/bash
sleep 5
# マイグレーション
python manage.py makemigrations
python manage.py migrate
# 静的ファイルの配置
python manage.py collectstatic --noinput
# uWSGIでデプロイ
uwsgi --socket :8001 --module serverproject.wsgi