from .base import *

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY='4-8p+vt=sr2$gc8gy9ylkp37x9t5k8=e&r^w_l+8qd@p6ib_t+' 

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