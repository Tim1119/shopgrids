import environ
from pathlib import Path
from pathlib import Path
import os
import logging.config
import logging
from django.utils.log import DEFAULT_LOGGING
import environ
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(DEBUG=(bool, False))


#---------------------------------------------------------- READING ENV FILES ---------------------------------------------------------
environ.Env.read_env(BASE_DIR / ".env")

#----------------------------------------------  PROJECT SETTINGS ---------------------------------------------------------------
SECRET_KEY=env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS=env('ALLOWED_HOSTS').split(" ")

#----------------------------------------------  APPLICATIONS --------------------------------------------------------------------

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    "apps.accounts",
]

THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",  
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.google',
    'django_celery_results',
    'django_celery_beat',
]

INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS +DJANGO_APPS

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'shopgrids.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shopgrids.wsgi.application'

AUTHENTICATION_BACKENDS = [
   
  'django.contrib.auth.backends.ModelBackend',  # Keep this for admin
'allauth.account.auth_backends.AuthenticationBackend',  # For allauth's authentication
    
]


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# -------------------------------------------------------- STATIC AND  MEDIA PATHS --------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static",]

MEDIA_URL = "/media/"



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ACCOUNT_FORMS = {
    'signup': 'apps.accounts.forms.CustomSignupForm',
}




# Enable email confirmation for signup
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Can be 'mandatory', 'optional', or 'none'

# Redirect URLs after email confirmation or other actions
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/login'  # Redirect to home if not logged in
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'  # Redirect after confirming email when logged in

# Email confirmation expiry time (default is 3 days)
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

# Enable/Disable email for password reset
ACCOUNT_PASSWORD_RESET_CONFIRMATION_EXPIRE_DAYS = 1

# Set a custom URL for email confirmation
ACCOUNT_EMAIL_CONFIRMATION_HMAC = True

# Enable email confirmation before login
ACCOUNT_AUTHENTICATED_REDIRECT_URL = '/'  # Redirect for authenticated users (after login)
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True  # Ask user to confirm their email during signup

# Prevent login until email is confirmed
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_VERIFICATION = 'mandatory' 


ACCOUNT_SIGNUP_REDIRECT_URL = '/login'  # Redirect to the homepage or custom page after successful signup

# Redirect after login
LOGIN_REDIRECT_URL = '/'  # After login, users are redirected here

# Redirect after logout
LOGOUT_REDIRECT_URL = '/login'  # After logout, users are redirected here

# Optional: Allow users to change their email address
ACCOUNT_ALLOW_EMAIL_CHANGE = False
AUTH_USER_MODEL = 'accounts.User'

ACCOUNT_AUTHENTICATION_METHOD = 'email'

# Since you're using email-only authentication, make sure username is not required
# ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_ADAPTER = 'apps.accounts.adapters.CustomAccountAdapter'
# Add or update these settings
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

# Add these new settings
SOCIALACCOUNT_AUTO_SIGNUP = False  # Disable automatic signup for social accounts
SOCIALACCOUNT_FORMS = {
    'signup': 'apps.accounts.forms.CustomSignupForm'
}


# settings.py

# -------------------------------------------------------- LOGS --------------------------------------------------
logger = logging.getLogger(__name__)

LOG_LEVEL = "INFO"

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
            },
            "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
            "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "console",
            },
            "file": {
                "level": "INFO",
                "class": "logging.FileHandler",
                "formatter": "file",
                "filename": "logs/shopgrids.log",
            },
            "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
        },
        "loggers": {
            "": {"level": "INFO", "handlers": ["console", "file"], "propagate": False},
            "apps": {"level": "INFO", "handlers": ["console"], "propagate": False},
            "django.server": DEFAULT_LOGGING["loggers"]["django.server"],
        },
    }
)
