'''
Run this with `$ python ./miny_django.py runserver` and go to http://localhost:8000/
'''
import os
import sys
from django.conf import settings

from django.conf.urls import patterns
from django.http import HttpResponse


# this module
me = os.path.splitext(os.path.split(__file__)[1])[0]
# helper function to locate this dir
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

# SETTINGS
DEBUG = True
ROOT_URLCONF = me
DATABASES = {'default': {}}  # required regardless of actual usage
TEMPLATE_DIRS = (here('.'), )
SECRET_KEY = 'so so secret'

if not settings.configured:
    settings.configure(**locals())

# Settings must be configured before importing
from django.views.decorators.csrf import csrf_exempt


# VIEW
@csrf_exempt
def index(request):
    return HttpResponse("Hello from mini_django.py")


# URLS
urlpatterns = patterns('', (r'^$', index))

if __name__ == '__main__':
    # set the ENV
    sys.path += (here('.'),)
    # run the development server
    from django.core import management
    management.execute_from_command_line()
