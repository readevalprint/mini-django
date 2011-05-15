'''
Run this with $ python ./micro_django.py and go to http://localhost:8000/Foo
'''

import os, sys
from django.conf.urls.defaults import patterns
from django.template.response import TemplateResponse

# this module
me = os.path.splitext(os.path.split(__file__)[1])[0]
# helper function to locate this dir
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

# SETTINGS
DEBUG=TEMPLATE_DEBUG=True
ROOT_URLCONF = me
DATABASES = { 'default': {} } #required regardless of actual usage
TEMPLATE_DIRS = (here('.'), )

# VIEW
def index(request, name):
    return TemplateResponse(request, 'index.html', {'name': name})

# URLS
urlpatterns = patterns('', (r'^(?P<name>\w+)?$', index))

if __name__=='__main__':
    # set the ENV
    os.environ['DJANGO_SETTINGS_MODULE'] = me
    sys.path += (here('.'),)
    # run the development server
    from django.core import management
    management.execute_from_command_line() 
