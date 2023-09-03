# external imports
from celery import shared_task

# internal imports
from util.email import send_email


@shared_task()
def send_email_on_birthday_task(email_address, username):
    '''
    Send an email on customer birthday

    :param email_address: recipient email address
    :param subject: email subject
    :param message: email body
    :return: None
    '''

    email_subject = "Happy Birthday"
    email_body = f"""
                Hi {username}
                Wish you many happy returns of the day :)
               """
    send_email(email_address, email_subject, email_body)
