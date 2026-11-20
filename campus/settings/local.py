from .base import *
# from decouple import config
# from dotenv import load_dotenv

#load_dotenv('.env')


ALLOWED_HOSTS = ['*']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = config('SECRET_KEY')

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