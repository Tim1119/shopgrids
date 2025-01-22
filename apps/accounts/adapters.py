# accounts/adapters.py

from allauth.account.adapter import DefaultAccountAdapter
from .tasks import send_confirmation_email
import logging

logger = logging.getLogger(__name__)

# accounts/adapters.py

class CustomAccountAdapter(DefaultAccountAdapter):
    def send_confirmation_mail(self, request, emailconfirmation, signup):
        logger.info("Generating confirmation URL")
        confirmation_url = self.get_email_confirmation_url(request, emailconfirmation)
        
        # Log the email address and confirmation URL
        logger.info(f"Sending confirmation email to {emailconfirmation.email_address.email} with URL: {confirmation_url}")
        
        send_confirmation_email.delay(emailconfirmation.email_address.email, confirmation_url)