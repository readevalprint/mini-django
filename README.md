Mini_django.py
==============

An entire django app in a single file. Updated from [here](http://olifante.blogs.com/covil/2010/04/minimal-django.html) to use Django trunk.

pico
====
This started off to see what the absolutely smallest requirements needed to run a Django project. Run the [pico_django.py](https://github.com/readevalprint/mini-django/blob/master/pico_django.py) with `$ PYTHONPATH=. django-admin.py runserver 0.0.0.0:8000 --settings=pico_django` and go to http://localhost:8000

Or with uwsgi in production:

    $ uwsgi --http :8000 -M --pythonpath=. \
    --env DJANGO_SETTINGS_MODULE=pico_django \
    -w "django.core.handlers.wsgi:WSGIHandler()"

mini
====
Soon pico needed a little more spice, so it got some template loading and then because I'm lazy I made the new version directly runnable.

Run the [mini_django.py](https://github.com/readevalprint/mini-django/blob/master/mini_django.py) with `$ python ./mini_django.py 0.0.0.0:8000` and go to http://localhost:8000/Foo

Dependencies
===========
* python
* django

Install
======
1. Clone this repo
2. `pip install requirements.txt`
3. Run
    1. `python ./mini_django.py runserver 0.0.0.0:8000`
    2. `PYTHONPATH=. django-admin.py runserver 0.0.0.0:8000 --settings=pico_django`


License
=======
As-is. Public Domain. Don't blame me.

Author
======
Tim Watts (tim@readevalprint.com)
