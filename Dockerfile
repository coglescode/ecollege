FROM python:3.10.6
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /capstone
COPY requirements.txt /capstone/
RUN pip install -r requirements.txt
COPY . /capstone/
#EXPOSE 8000
#CMD [ "python3", " manage.py", " runserver", "0.0.0.0:8000" ]

 
