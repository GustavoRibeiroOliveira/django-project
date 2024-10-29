#!bin/sh

cd /code

python manage.py migrate
python manage.py runserver