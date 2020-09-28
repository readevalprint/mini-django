from django.http import HttpResponse
from django.urls import path


DEBUG = True
ROOT_URLCONF = 'pico_django'
ALLOWED_HOSTS = '*'
DATABASES = {'default': {}}


def index(request, name=None):
    return HttpResponse('Hello {name}!'.format(name=(name or 'World')))

urlpatterns = [
    path('', index),
    path('<str:name>', index)
]

SECRET_KEY = "not so secret"

# run with djagno dev server
# $ PYTHONPATH=. django-admin.py runserver 0.0.0.0:8000 --settings=pico_django

# for example run with uWSGI
# $ uwsgi --http :8000 -M --pythonpath=. --env DJANGO_SETTINGS_MODULE=pico_django -w "django.core.wsgi:get_wsgi_application()"
