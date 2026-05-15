import os
from .base import *
from decouple import config 
from dotenv import load_dotenv

load_dotenv('.env')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG_PROD')
SECRET_KEY = os.getenv('SECRET_KEY_PROD')

#ADMINS = [
#    ('Antonio M', 'email@mydomain.com'),
#]

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS_PROD', '').split(',')
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS_PROD', '').split(',')

DATABASE_SCHEMAS = ['test', 'public']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.getenv('POSTGRES_DB'),
       'USER': os.getenv('POSTGRES_USER'),
       'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
       'HOST': os.getenv('POSTGRES_HOST'),
       'PORT': os.getenv('POSTGRES_PORT'),
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