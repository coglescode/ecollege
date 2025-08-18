#!/bin/bash

#python manage.py collectstatic --noinput
python manage.py makemigrations --settings=capstone.settings.production --noinput
python manage.py migrate --settings=capstone.settings.production --noinput

python manage.py runserver 0.0.0.0:8001 --settings=capstone.settings.production

# if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
#     python manage.py createsuperuser --noinput || true
# fi

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8001" ]

uwsgi --http :8001 --module capstone.wsgi:application --env DJANGO_SETTINGS_MODULE=capstone.settings.production

#uwsgi --ini /app/uwsgi.ini
