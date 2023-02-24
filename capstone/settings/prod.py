import os
from .base import *
from decouple import config 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

#ADMINS = [
#    ('Antonio M', 'email@mydomain.com'),
#]

ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
