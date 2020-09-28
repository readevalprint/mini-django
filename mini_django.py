"""
Run with `python mini_django.py runserver` and go to http://localhost:8000/.
"""
from os.path import abspath, dirname, join

import django
from django.conf import settings
from django.urls import path
from django.shortcuts import render


# SETTINGS
BASE_DIR = dirname(abspath(__file__))
DEBUG = True
ROOT_URLCONF = "mini_django"  # this module
DATABASES = {"default": {}}  # required regardless of actual usage
TEMPLATES = [
    {"BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": [BASE_DIR,]}
]
STATIC_URL = "/static/"
STATICFILES_DIRS = (join(BASE_DIR, "static"),)
SECRET_KEY = "not so secret",

SETTINGS = dict((key,val) for key, val in locals().items() if key.isupper())
if not settings.configured:
    settings.configure(**SETTINGS)
django.setup()


# Settings must be configured before importing some things like staticfiles
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



# VIEW

def index(request, name=None):
    return render(request, "index.html", {"name": name})



# URLS

urlpatterns = [
    path("", index),
    path("<str:name>", index, name="named")
]
urlpatterns += staticfiles_urlpatterns()



# CLI

if __name__ == "__main__":
    # make this script runnable like a normal `manage.py` command line script.
    from django.core import management
    management.execute_from_command_line()
