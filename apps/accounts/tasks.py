from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import logging



@shared_task
def send_confirmation_email(to_email, confirmation_link):
    try:
        logger = logging.getLogger(__name__)
        logger.info(f"Attempting to send confirmation email to {to_email}")
        subject = 'Confirm your Email Address'
        from_email = settings.DEFAULT_FROM_EMAIL
        
        # Context for the template
        context = {
            'confirmation_link': confirmation_link,
            'site_name': 'ShopGrids',
            'support_email': settings.DEFAULT_FROM_EMAIL,
        }
        
        # Render HTML content
        html_content = render_to_string('emails/email_confirmation.html', context)
        # Create plain text version by stripping HTML
        text_content = strip_tags(html_content)
        
        # Create email
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=from_email,
            to=[to_email]
        )
        
        # Attach HTML content
        email.attach_alternative(html_content, "text/html")
        
        # Send email
        email.send()

    except Exception as e:
        logger.error(f"Failed to send confirmation email to {to_email}: {str(e)}")
        raise