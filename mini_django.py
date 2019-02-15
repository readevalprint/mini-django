from django.urls import path
from django.shortcuts import render
'''
Run this with `$ python ./mini_django.py runserver` and go
to http://localhost:8000/
'''
import os
import sys
from django.conf import settings


# this module
me = os.path.splitext(os.path.split(__file__)[1])[0]

# helper function to locate this dir
def here(x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), x)


# SETTINGS
DEBUG = True
ROOT_URLCONF = me
DATABASES = {'default': {}}  # required regardless of actual usage


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': here('.'),
    },
]
SECRET_KEY = 'so so secret'
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
)
INSTALLED_APPS = (
    'django.contrib.sessions',
)
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    here('static'),
)


if not settings.configured:
    settings.configure(**locals())

# Settings must be configured before importing some things like static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# VIEW
def index(request, name=None):
    return render(request, 'index.html', {'name': name})

# URLS

urlpatterns = [
    path('', index),
    path('<str:name>', index)
]

urlpatterns += staticfiles_urlpatterns()

if __name__ == '__main__':
    # set the ENV
    sys.path += (here('.'),)
    # run the development server
    from django.core import management
    management.execute_from_command_line()
