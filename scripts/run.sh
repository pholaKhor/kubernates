#!/bin/sh
set -e

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata patient.json 
python manage.py loaddata doctor.json 
python manage.py loaddata claim.json 
gunicorn -b :8080 --chdir /app app.wsgi:application
