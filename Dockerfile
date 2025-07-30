# Pull official base Python Docker image
FROM python:3.12

# Set enviroment variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /src

# Install dependencies
COPY requirements.txt /src/
#COPY manage.py /src/
#RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /src/

ENV DJANGO_SETTINGS_MODULE=capstone.settings

EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

 
