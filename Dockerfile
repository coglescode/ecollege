# Dockerfile for ecollege
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY requirements.txt /src/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /src/

ENV DJANGO_SETTINGS_MODULE=capstone.settings.production

EXPOSE 8001
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8001" ]

 
