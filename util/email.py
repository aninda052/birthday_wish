# external imports
from django.core.mail import send_mail
from django.conf import settings


def send_email(email_address, email_subject, email_body):
    '''
    Sent email to the given recipient

    :param email_address: recipient email address
    :param email_subject: email subject
    :param email_body: email body
    :return: None
    '''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_address ]
    send_mail(email_subject, email_body, email_from, recipient_list)