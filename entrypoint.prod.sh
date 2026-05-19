#!/bin/bash

# Make sure the environment settings value is set to production
# DJANGO_SETTINGS_MODULE=capstone.settings.production
#source /app/venv/bin/activate

#python manage.py collectstatic --noinput
#python manage.py makemigrations --settings=capstone.settings.local --noinput
#python manage.py migrate --settings=capstone.settings.local --noinput

python manage.py makemigrations --settings=capstone.settings.prod --noinput
python manage.py migrate --settings=capstone.settings.prod --noinput

#python manage.py runserver --settings=capstone.settings.production 0.0.0.0:8000
# if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
#     python manage.py createsuperuser --noinput || true
# fi

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8001" ]

#uwsgi --http :8000 \
#      --module capstone.wsgi:application --env DJANGO_SETTINGS_MODULE=capstone.settings.local \
#      --master --processes 4 --threads 2 --buffer-size 32768 \
#      --socket 172.18.0.2:8000 \
#      --protocol=http \
#      --vacuum \

uwsgi --http :8001 --module capstone.wsgi:application --env DJANGO_SETTINGS_MODULE=capstone.settings.prod
