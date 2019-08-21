from django.conf.urls import url
from django.conf import settings
import os

DEBUG = True
ROOT_URLCONF = "mini_api"
ALLOWED_HOSTS = "*"
DATABASES = {"default": {}}
SECRET_KEY = "not so secret"
INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "rest_framework",
)
# helper function to locate this dir
def here(x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), x)


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": here("."),
        "APP_DIRS": True,
    }
]

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    here('static'),
)



if not settings.configured:
    settings.configure(**locals())

# Settings must be configured before importing some things like staticfiles
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.response import Response
from rest_framework.views import APIView


class Index(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    authentication_classes = ()
    permission_classes = ()

    def get(self, request, name, format=None):
        """
        Return a list of all users.
        """
        return Response("hi " + (name or "World!!"))


urlpatterns = [url(r"^(?P<name>\w+)?$", Index.as_view())]
urlpatterns += staticfiles_urlpatterns()


# run with djagno dev server
# $ PYTHONPATH=. django-admin.py runserver 0.0.0.0:8000 --settings=mini_api

# for example run with uwsgi
# `$ uwsgi --http :8000 -M --pythonpath=. --env DJANGO_SETTINGS_MODULE=mini_api -w "django.core.handlers.wsgi:WSGIHandler()"`
