# external imports
from django.db import models
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string

# internal imports
from .tasks import set_schedule_for_birthday_wish_task


# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, null=False)
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=False)

    def __str__(self):
        return self.email

    def assign_new_username(self):
        username = self.email.split('@')[0]
        new_username = username
        while type(self).objects.filter(username=new_username).exists():
            random_str = get_random_string(length=2, allowed_chars='0123456789')
            new_username = username + random_str

        self.username = new_username

    def save(self, new_customer=False, *args, **kwargs, ):
        if not self.username:
            self.assign_new_username()
            new_customer = True

        super().save(*args, **kwargs)

        if new_customer:
            set_schedule_for_birthday_wish_task.delay(self.email, self.date_of_birth, self.username)

# def assign_username(sender, instance, **kwargs):
#     '''
#     Before creating a new customer object, assign a unique username
#     for the customer object
#     :param sender:
#     :param instance:
#     :param kwargs:
#     :return:
#     '''
#
#     # True only if this is new instance
#     # meaning object is not yet created nor it's an update operation
#     if not instance.id:
#         username = instance.email.split('@')[0]
#         new_username = username
#         while sender.objects.filter(username=new_username).exists():
#             random_str = get_random_string(length=2, allowed_chars='0123456789')
#             new_username = username + random_str
#
#         instance.username = new_username
#         set_schedule_for_birthday_wish_task.delay(instance.email, instance.date_of_birth, new_username)
#
#
# pre_save.connect(assign_username, sender=Customer)
