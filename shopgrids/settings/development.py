from .base import *

MEDIA_ROOT = [BASE_DIR / 'mediafiles']

ACCOUNT_ADAPTER = 'apps.accounts.adapters.CustomAccountAdapter'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = env('DEVELOPMENT_EMAIL_HOST')  # e.g., 'smtp.gmail.com'
# EMAIL_PORT = env('DEVELOPMENT_EMAIL_PORT')  # e.g., 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = env('DEVELOPMENT_EMAIL_HOST_USER')  # Your email address
# EMAIL_HOST_PASSWORD = env('DEVELOPMENT_EMAIL_HOST_PASSWORD')  # Your email password/app password
DEFAULT_FROM_EMAIL = env('DEVELOPMENT_DEFAULT_FROM_EMAIL')  # Your default from email
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '3fae8e0228c719'
EMAIL_HOST_PASSWORD = '19aea0da8b1aa1'
EMAIL_PORT = '2525'



# CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='redis://localhost:6379/0')
# CELERY_RESULT_BACKEND = 'django-db'

CELERY_BROKER_URL = 'amqp://localhost'  
CELERY_RESULT_BACKEND = 'rpc://'   
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Lagos'


