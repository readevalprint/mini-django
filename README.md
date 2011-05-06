An entire django app in a single file. Updated from [here](http://olifante.blogs.com/covil/2010/04/minimal-django.html) to use Django trunk. 

This started off to see what the absolutely smallest requirements needed to run a Django project. run the following with `$ PYTHONPATH=. django-admin.py runserver 0.0.0.0:8000 --settings=pico_django`

    from django.http import HttpResponse
    from django.conf.urls.defaults import patterns
    
    DEBUG=True
    ROOT_URLCONF = 'pico_django'
    DATABASES = { 'default': {} }
    def index(request, name):
        return HttpResponse('Hello {name}!'.format(name=(name or 'World')))
    
    urlpatterns = patterns('', (r'^(?P<name>\w+)?$', index))