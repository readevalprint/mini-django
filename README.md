Mini_django.py
==============

An entire django app in a single file. Updated from [here](http://olifante.blogs.com/covil/2010/04/minimal-django.html) to use Django trunk. 

pico
====
This started off to see what the absolutely smallest requirements needed to run a Django project. Run the [pico_django.py](https://github.com/readevalprint/mini-django/blob/master/pico_django.py) with `$ PYTHONPATH=. django-admin.py runserver 0.0.0.0:8000 --settings=pico_django` and go to http://localhost:8080

    from django.http import HttpResponse
    from django.conf.urls.defaults import patterns
    
    DEBUG=True
    ROOT_URLCONF = 'pico_django'
    DATABASES = { 'default': {} }
    def index(request, name):
        return HttpResponse('Hello {name}!'.format(name=(name or 'World')))
    
    urlpatterns = patterns('', (r'^(?P<name>\w+)?$', index))

mini
====
Soon pico needed a little more spice, so it got some template loading and then because I'm lazy I made the new version directly runnable.

Run the [mini_django.py](https://github.com/readevalprint/mini-django/blob/master/mini_django.py) with `$ python ./micro_django.py` and go to http://localhost:8000/Foo


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


Dependencies
===========
* python
* django

Install
======
1. Install [django](http://docs.djangoproject.com/en/dev/intro/install/)
2. get the [code](https://github.com/readevalprint/mini-django/raw/master/mini_django.py) `wget https://github.com/readevalprint/mini-django/raw/master/mini_django.py`
3. run it `$ python ./mini_django.py`
4. open browser http://localhost.com/Foo

License
=======
As-is. Public Domain. Don't blame me.

Author
======
Tim Watts (tim@readevalprint.com)
