[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/readevalprint/mini-django)



Mini_django.py
==============

An entire django app in a single file. Updated from [here](http://olifante.blogs.com/covil/2010/04/minimal-django.html) to use Django trunk.
Works with Django 1.1 and 2.1.

pico
====
This started off to see what the absolutely smallest requirements needed to run a Django project. Run the [pico_django.py](https://github.com/readevalprint/mini-django/blob/master/pico_django.py) with `$ PYTHONPATH=. django-admin.py runserver 0.0.0.0:8000 --settings=pico_django` and go to http://localhost:8000

Or with uwsgi in production:

    $ uwsgi --http :8000 -M --pythonpath=. 
    --env DJANGO_SETTINGS_MODULE=pico_django \
    -w "django.core.wsgi:get_wsgi_application()"

mini
====
Soon pico needed a little more spice, so it got some template loading and then because I'm lazy I made the new version directly runnable. Run the [mini_django.py](https://github.com/readevalprint/mini-django/blob/master/mini_django.py) with 

    $ python ./mini_django.py runserver 0.0.0.0:8000
    
and go to http://localhost:8000/Foo


api
===

Often I need to use django-rest-framework for a simple one-off task, thankfully, mini_django can be adapted quite easily into [mini_api.py](https://github.com/readevalprint/mini-django/blob/master/mini_api.py)

    $ python ./mini_api.py runserver 0.0.0.0:8000
    
and go to http://localhost:8000


Dependencies
===========
* python
* django
* [uWSGI](https://uwsgi-docs.readthedocs.io) (optional)
* [django rest framework](http://django-rest-framework.org) (optional)

Install
======
1. Clone this repo
2. `pip install django`
3. Run
    1. `python ./mini_django.py runserver 0.0.0.0:8000`
    2. `PYTHONPATH=. django-admin.py runserver 0.0.0.0:8000 --settings=pico_django`


License
=======
As-is. Public Domain. Don't blame me.

Author
======
Tim Watts (tim@readevalprint.com) [@readevalprint](https://twitter.com/readevalprint)
