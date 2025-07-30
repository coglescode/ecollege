import os
from .base import *
from decouple import config 

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = os.getenv('DEBUG')
DEBUG = False
SECRET_KEY='4-8p+vt=sr2$gc8gy9ylkp37x9t5k8=e&r^w_l+8qd@p6ib_t+' 

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

# DATABASES = {   
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     } 
# }