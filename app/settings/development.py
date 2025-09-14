from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vigia',
        'USER': 'postgres',
        'PASSWORD': 'example',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

CORS_ALLOW_ALL_ORIGINS = True

