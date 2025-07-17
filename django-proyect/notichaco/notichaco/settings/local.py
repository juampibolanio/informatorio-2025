from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'notichaco',
        'USER': 'root',
        'PASSWORD': 'juampi123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}