# external imports
from django.db import models
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string
from django.conf import settings
from django_celery_beat.models import CrontabSchedule, PeriodicTask
import json

# internal imports

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, null=False)
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



def create_username(sender, instance, created, **kwargs):
    if created:
        username = instance.email.split('@')[0]
        new_username = username
        while sender.objects.filter(username=new_username).exists():
            random_str = get_random_string(length=2, allowed_chars='0123456789')
            new_username = username + random_str

        instance.username = new_username
        instance.save()

        birthday_schedule, _ = CrontabSchedule.objects.get_or_create(
            minute='00',
            hour='00',
            day_of_month=instance.date_of_birth.day,
            month_of_year=instance.date_of_birth.month,
            timezone=settings.TIME_ZONE
        )

        PeriodicTask.objects.create(
            crontab=birthday_schedule,
            name=f'birthday_schedule_for_{new_username}',
            task='customer.tasks.send_email_on_birthday_task',
            kwargs=json.dumps(
                {
                    "email_address": instance.email,
                    "username": new_username,
                }
            ),
        )


post_save.connect(create_username, sender=Customer)
