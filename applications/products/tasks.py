from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model


User = get_user_model()


@shared_task
def send_email():
    emails = User.objects.values_list('email', flat=True)
    return send_mail(
        subject="New product!",
        message="Hello! There is new product on site! Go Get it"
    )
