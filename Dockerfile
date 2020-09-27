FROM python:3.7-alpine

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

# Run mini_django using Django's dev server
CMD python mini_django.py runserver 0.0.0.0:${PORT:-8000}

# uncomment the line below to run the mini_api server instead
# CMD python mini_api.py runserver 0.0.0.0:${PORT:-8000}
