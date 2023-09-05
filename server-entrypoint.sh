#!/bin/bash

python manage.py makemigrations
python manage.py migrate --no-input

# create initial superuser.
# Login to Django admin panel, create a new user with
# superuser status and delete this initial superuser
DJANGO_SUPERUSER_PASSWORD=admin DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@email.com python manage.py createsuperuser --noinput

python manage.py runserver 0.0.0.0:8000