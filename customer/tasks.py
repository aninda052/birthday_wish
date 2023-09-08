# external imports
from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from django_celery_beat.models import CrontabSchedule, PeriodicTask
import json

# internal imports
from util.email import send_email


logger = get_task_logger(__name__)

def log_celery_task_failure(self, exc, task_id, args, kwargs, einfo):
    logger.error(f"task [{task_id}] failed with billow kwargs")
    logger.error(f"[{task_id}] {kwargs}")


@shared_task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 3, 'countdown': 10}, on_failure=log_celery_task_failure)
def send_email_on_birthday_task(email_address, username):
    '''
    Send an email on customer birthday

    :param email_address: recipient email address
    :param subject: email subject
    :param message: email body
    :return: None
    '''
    logger.info(f"sending birthday wish to {username}")

    email_subject = "Happy Birthday"
    email_body = f"""
                Hi {username}
                Wish you many happy returns of the day :)
               """
... # this line will through error without valid email credential
    send_email(email_address, email_subject, email_body)


@shared_task()
def set_schedule_for_birthday_wish_task(email_address, date_of_birth, username):
    '''
    Set a schedule task on customer birthday for customer

    :param email_address: customer email address
    :param date_of_birth: customer date of birth
    :param username: customer username
    :return: None
    '''

    logger.info(f"schedule job for {username}")

    birthday_schedule, _ = CrontabSchedule.objects.get_or_create(
        minute='0',
        hour='00',
        day_of_month=date_of_birth.day,
        month_of_year=date_of_birth.month,
        timezone=settings.TIME_ZONE
    )

    PeriodicTask.objects.create(
        crontab=birthday_schedule,
        name=f'birthday_schedule_for_{username}',
        task='customer.tasks.send_email_on_birthday_task',
        kwargs=json.dumps(
            {
                "email_address": email_address,
                "username": username,
            }
        ),
    )