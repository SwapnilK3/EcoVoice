from django.conf import settings
from django.core.mail import send_mail


def send_email_token(email, token):
   
        subject = 'Your email verification token'
        message = f'Your email verification token is http://127.0.0.1:8000/charity/verify/{token}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        
