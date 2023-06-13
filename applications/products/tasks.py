from celery import shared_task


@shared_task
def send_email():
    return 1 + 1
