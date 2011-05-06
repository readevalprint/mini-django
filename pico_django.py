from django.http import HttpResponse
from django.conf.urls.defaults import patterns
DEBUG=True
ROOT_URLCONF = 'pico_django'
DATABASES = { 'default': {} }
def index(request, name):
    return HttpResponse('Hello {name}!'.format(name=(name or 'World')))

urlpatterns = patterns('', (r'^(?P<name>\w+)?$', index))

# run with djagno dev server
# $ PYTHONPATH=. django-admin.py runserver 0.0.0.0:8000 --settings=pico_django

# for example run with uwsgi
# $ uwsgi -s 127.0.0.1:3031 -M --pythonpath=/path/to/this/dir --env DJANGO_SETTINGS_MODULE=pico_django -w "django.core.handlers.wsgi:WSGIHandler()"

