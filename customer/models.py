# external imports
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string
# Create your models here.

class Customer(AbstractUser):
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

post_save.connect(create_username, sender=Customer)
