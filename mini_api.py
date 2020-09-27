"""
Run with `python mini_api.py runserver` and go to http://localhost:8000/.
"""
from os.path import abspath, dirname, join

import django
from django.conf import settings
from django.urls import re_path



# SETTINGS
BASE_DIR = dirname(abspath(__file__))
DEBUG = True
ROOT_URLCONF = "mini_api"  # this module
ALLOWED_HOSTS = "*"
DATABASES = {"default": {}}
SECRET_KEY = "not so secret"
INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "rest_framework",
)
TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates",
              "DIRS": [BASE_DIR,], "APP_DIRS": True}]
STATIC_URL = '/static/'
STATICFILES_DIRS = (join(BASE_DIR, 'static'),)

SETTINGS = dict((key,val) for key, val in locals().items() if key.isupper())
if not settings.configured:
    settings.configure(**SETTINGS)
django.setup()

# Settings must be configured before importing some things like staticfiles
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.response import Response
from rest_framework.views import APIView



# VIEWS

class Index(APIView):
    """
    Respond with a greeting for a user or the whole world!
    """
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, name=None, format=None):
        return Response("hi " + (name or "World!!"))



# URLS

urlpatterns = [
    re_path(r"^(?P<name>\w+)?$", Index.as_view())
]
urlpatterns += staticfiles_urlpatterns()



# CLI

if __name__ == "__main__":
    # make this script runnable like the ./manage.py command line script
    from django.core import management
    management.execute_from_command_line()
