# myapp/signals.py

from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from .tasks import send_email_task

@receiver(user_signed_up)
def user_signed_up_handler(request, user, **kwargs):
    subject = 'Welcome to My Site'
    message = 'Thank you for signing up!'
    from_email = 'no-reply@mysite.com'
    recipient_list = [user.email]
    
    # Call the Celery task
    send_email_task.delay(subject, message, from_email, recipient_list)