from django.http import HttpResponse
from django.conf.urls import url

DEBUG = True
ROOT_URLCONF = 'pico_django'
ALLOWED_HOSTS = '*'
DATABASES = {'default': {}}


def index(request, name):
    return HttpResponse('Hello {name}!'.format(name=(name or 'World')))

urlpatterns = [
    url(r'^(?P<name>\w+)?$', index)
]

SECRET_KEY = "not so secret"

# run with djagno dev server
# $ PYTHONPATH=. django-admin.py runserver 0.0.0.0:8000 --settings=pico_django

# for example run with uwsgi
# `$ uwsgi --http :8000 -M --pythonpath=. --env DJANGO_SETTINGS_MODULE=pico_django -w "django.core.handlers.wsgi:WSGIHandler()"`
