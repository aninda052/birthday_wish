from celery.signals import setup_logging
from celery import Celery
import logging
import os

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birthday_wish.settings')

app = Celery('birthday_wish')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@setup_logging.connect
def setup_celery_logging(**kwargs):
    return logging.getLogger('celery')
