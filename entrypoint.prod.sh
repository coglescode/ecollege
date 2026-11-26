#!/bin/bash

# Make sure the environment settings value is set to production

#python manage.py collectstatic --settings=campus.settings.local --noinput
#python manage.py makemigrations ecollege --settings=campus.settings.local --noinput
python manage.py migrate --settings=campus.settings.local --noinput

#python manage.py runserver --settings=ecollege.settings.production 0.0.0.0:8000
# if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
#     python manage.py createsuperuser --noinput || true
# fi


#uwsgi --http :8000 \
#      --module ecollege.wsgi:application --env DJANGO_SETTINGS_MODULE=ecollege.settings.local \
#      --master --processes 4 --threads 2 --buffer-size 32768 \
#      --socket 172.18.0.2:8000 \
#      --protocol=http \
#      --vacuum \


gunicorn campus.wsgi --env DJANGO_SETTINGS_MODULE=campus.settings.local -b :8000