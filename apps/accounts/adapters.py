# accounts/adapters.py

from allauth.account.adapter import DefaultAccountAdapter
from .tasks import send_confirmation_email
import logging

logger = logging.getLogger(__name__)

# accounts/adapters.py

# class CustomAccountAdapter(DefaultAccountAdapter):
#     def send_confirmation_mail(self, request, emailconfirmation, signup):
#         logger.info("Generating confirmation URL")
#         confirmation_url = self.get_email_confirmation_url(request, emailconfirmation)
        
#         # Log the email address and confirmation URL
#         logger.info(f"Sending confirmation email to {emailconfirmation.email_address.email} with URL: {confirmation_url}")
        
#         send_confirmation_email.delay(emailconfirmation.email_address.email, confirmation_url)

# In a custom adapter file
from allauth.account.adapter import DefaultAccountAdapter

from allauth.account.adapter import DefaultAccountAdapter

from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.sites.shortcuts import get_current_site

class CustomAccountAdapter(DefaultAccountAdapter):

    
   def send_mail(self, template_prefix: str, email: str, context: dict) -> None:
    try:
        # Create a global context dictionary if it doesn't exist
        if 'context' not in globals():
            globals()['context'] = type('GlobalContext', (), {})()
        
        # Attempt to get the request from the global context
        request = globals()["context"].request
        
        # Prepare the email context
        ctx = {
            "request": request,
            "email": email,
            "current_site": get_current_site(request),
        }
        ctx.update(context)
        
        # Render and send the mail
        msg = self.render_mail(template_prefix, email, ctx)
        msg.content_subtype = 'html'  # Ensure HTML content type
        msg.send()
    
    except Exception as e:
        # Fallback to default method if request retrieval fails
        super().send_mail(template_prefix, email, context)

# In settings.py
# ACCOUNT_ADAPTER = 'path.to.your.CustomAccountAdapter'