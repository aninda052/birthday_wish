#!/bin/bash

python manage.py makemigrations
python manage.py migrate --no-input
celery -A birthday_wish beat -l info