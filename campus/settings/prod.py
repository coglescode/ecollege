import os
from .base import *
from decouple import config 
from dotenv import load_dotenv

load_dotenv('.env')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')

#ADMINS = [
#    ('Antonio M', 'email@mydomain.com'),
#]

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default= '').split(',')

DATABASE_SCHEMAS = ['test', 'public']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': config('POSTGRES_DB'),
       'USER': config('POSTGRES_USER'),
       'PASSWORD': config('POSTGRES_PASSWORD'),
       'HOST': config('POSTGRES_HOST'),
       'PORT': config('POSTGRES_PORT'),
       'OPTIONS': {
           'options': f"-c search_path={','.join(DATABASE_SCHEMAS)}"
       }
   }
}

# HTTPS Settings in setting.py
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS Settings
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 31563000
SECURE_HSTS_RELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True