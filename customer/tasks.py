# external imports
from celery import shared_task
from celery.utils.log import get_task_logger

# internal imports
from util.email import send_email


logger = get_task_logger(__name__)

@shared_task()
def send_email_on_birthday_task(email_address, username):
    '''
    Send an email on customer birthday

    :param email_address: recipient email address
    :param subject: email subject
    :param message: email body
    :return: None
    '''
    logger.info(f"sending birthday wish for {username}")

    email_subject = "Happy Birthday"
    email_body = f"""
                Hi {username}
                Wish you many happy returns of the day :)
               """
    send_email(email_address, email_subject, email_body)
