from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vigia',
        'USER': 'root',
        'PASSWORD': 'example',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

CORS_ALLOW_ALL_ORIGINS = True

