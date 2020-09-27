[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/readevalprint/mini-django)

Mini-Django
===========
An entire django app in a single file. Updated from [here](http://olifante.blogs.com/covil/2010/04/minimal-django.html) to use Django trunk. Works with Django 1.11, 2.x, and 3.x.


Quick Start
===========

Clone https://github.com/readevalprint/mini-django

    $ docker build . -t mini-django
    $ docker run -p 8000:8000 -v `pwd`:/app mini-django

and go to http://localhost:8000/Foo. You can change the code in `mini_django.py`
and the server will automatically reload as soon as you save your changes.


Dependencies
============
* python3
* django
* [uWSGI](https://uwsgi-docs.readthedocs.io) (optional)
* [django rest framework](http://django-rest-framework.org) (optional)


Install
=======
1. Clone this repo
2. (optional) Create a virtualenv `virtualenv -p python3 venv`
   and activate it using `source venv/bin/activate`.
3. Install Python dependencies `pip install -r requirements.txt`
4. You can now run the three sample servers using one of the commands below:
   - `PYTHONPATH=. django-admin.py runserver 0.0.0.0:8000 --settings=pico_django`
   - `python mini_django.py runserver`
   - `python mini_api.py runserver`



pico
====
This started off to see what the absolutely smallest requirements needed to run a Django project. Run the [pico_django.py](https://github.com/readevalprint/mini-django/blob/master/pico_django.py) with:

    $ PYTHONPATH=. django-admin.py runserver 0.0.0.0:8000 --settings=pico_django

You can then go to http://localhost:8000 to see the running server.


mini
====
Soon pico needed a little more spice, so it got some template loading and then because I'm lazy I made the new version directly runnable. Run the [mini_django.py](https://github.com/readevalprint/mini-django/blob/master/mini_django.py) with 

    $ python mini_django.py runserver
    
and go to http://localhost:8000/Foo


api
===
Often I need to use django-rest-framework for a simple one-off task, thankfully, mini_django can be adapted quite easily into [mini_api.py](https://github.com/readevalprint/mini-django/blob/master/mini_api.py)

    $ python mini_api.py runserver
    
and go to http://localhost:8000



Production
==========
You can also run these Django projects in production-like mode using a WSGI server
like `uWSGI` or `gunicorn`.

uWSGI
-----
First run `pip install uwsgi` to install the uWSGI package (requires build tools).
You can then start the server using:

    $ uwsgi --http :8000 -M --pythonpath=. \
        --env DJANGO_SETTINGS_MODULE=mini_django \
        -w "django.core.wsgi:get_wsgi_application()"

Replace `mini_django` with `pico_django` or `mini_api` to run the other projects.

gunicorn
--------
First install gunicorn using `pip install gunicorn`, then start the server using:

    $ gunicorn --bind 0.0.0.0:8000 \
        --env DJANGO_SETTINGS_MODULE=mini_django \
        "django.core.wsgi:get_wsgi_application()"


Replace `mini_django` with `pico_django` or `mini_api` to run the other projects.


Disclaimer
----------
Note the above "production" examples are only given as POC to show the code works
and not recommended for use in a real production environment. You'd need to think
about number of WSGI workers, using NGINX to serve static files, and other such.



License
=======
As-is. Public Domain. Don't blame me.


Author
======
Tim Watts (tim@readevalprint.com) [@readevalprint](https://twitter.com/readevalprint)


Contributors
============
Ivan Savov (ivan@minireference.com) [@minireference](https://twitter.com/minireference)

