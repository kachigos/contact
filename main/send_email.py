from django.core.mail import send_mail
from .models import Contact


def send_contact(data):

    to_email = 'chyngyzsubhanov@gmail.com'
    send_mail(
        'Subject',
        f'{data}',
        'from@example.com',
        [to_email],
        fail_silently=False
    )