from django.core import mail
from django.core.mail import EmailMessage
from django.template.loader import get_template


class Mailer:

    def __init__(self, from_email=None):

        self.connection = mail.get_connection()
        self.from_email = from_email

