#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Wait for the database
./wait-for-it.sh db:5432 -- echo "Database is up"

# Run Django commands in sequence
python manage.py makemigrations ecollege usertype
python manage.py migrate

# Uncomment if you need to create a superuser
# python manage.py createsuperuser --noinput


# Start the development server
exec python manage.py runserver 0.0.0.0:8001
