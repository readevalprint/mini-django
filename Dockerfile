FROM python:3.7-alpine

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app
CMD python ./mini_django.py runserver 0.0.0.0:${PORT:-8000}
