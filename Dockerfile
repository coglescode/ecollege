# Dockerfile for ecollege
FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /src

# COPY requirements.txt /src/
COPY . /src/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt



# ENV DJANGO_SETTINGS_MODULE=capstone.settings.production
ENV DJANGO_SETTINGS_MODULE=capstone.settings.local

RUN python manage.py makemigrations ecollege usertype && \
    python manage.py migrate
#    python manage.py createsuperuser --noinput

EXPOSE 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]

 
