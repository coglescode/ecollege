import os

from .base import *


ALLOWED_HOSTS = ['*']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# DATABASE_ROUTERS = ['coglescode_com.db_routers.AuthRouter', 'coglescode_com.db_routers.PortfolioRouter','coglescode_com.db_routers.BlogRouter',]
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASE_SCHEMAS = ['campus', 'public']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.environ['POSTGRES_DB'],
       'USER': os.environ['POSTGRES_USER'],
       'PASSWORD': os.environ['POSTGRES_PASSWORD'],
       'HOST': os.environ['POSTGRES_HOST'],
       'PORT': os.environ['POSTGRES_PORT'],
       'OPTIONS': {
           'options': f"-c search_path={','.join(DATABASE_SCHEMAS)}"
       }
   }
}