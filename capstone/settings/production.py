import os
from .base import *
from decouple import config 
from dotenv import load_dotenv

load_dotenv('.env')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')
SECRET_KEY = os.getenv('SECRET_KEY')

#ADMINS = [
#    ('Antonio M', 'email@mydomain.com'),
#]

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', '').split(',')

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
