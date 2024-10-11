
FROM python:3.12-alpine

#WORKDIR /usr/Esummit23-backend

ENV PYTHONBUFFERED 1



RUN pip install --upgrade pip \
  && pip install --upgrade setuptools \
  && pip install --upgrade pipenv  \
  && pip install --upgrade boto3 \
  && pip install --upgrade django-storages \
  && pip install gevent

#  && pip install psycopg2


COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /backend
WORKDIR /backend 

COPY . .

CMD ["sh", "-c", "python manage.py collectstatic --no-input;python manage.py makemigrations;python manage.py migrate;gunicorn astrology_project.wsgi:application -b 0.0.0.0:8000  --timeout 120  "]