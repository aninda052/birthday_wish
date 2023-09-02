# external imports
from django.db import models
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
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
        send_email(instance.email, new_username)

post_save.connect(create_username, sender=Customer)


def send_email(email_address, username):
    subject = 'Happy Birthday!!!'
    message = f'Hi {username}, Happy Birthday to you'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_address ]
    send_mail(subject, message, email_from, recipient_list)