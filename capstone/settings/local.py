from .base import *

ALLOWED_HOSTS = ['192.168.2.207', 'ecollege.coglescode.com', '*']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = os.getenv('SECRET_KEY')

#SECRET_KEY = os.environ.get('SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# DATABASE_ROUTERS = ['coglescode_com.db_routers.AuthRouter', 'coglescode_com.db_routers.PortfolioRouter','coglescode_com.db_routers.BlogRouter',]
DATABASES = {   
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } 
}