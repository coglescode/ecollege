# Dockerfile for ecollege
FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY requirements.txt /src//
RUN pip install -r requirements.txt

COPY . /src/

EXPOSE 8001
CMD [ "python3", " manage.py", " runserver", "0.0.0.0:8001" ]

 
