=======
Gondola
=======


Gondola is a very simple Django app to present in an elegant grid categories, sections, product ranges...
or whatever on a html page, ideally a homepage.

Fully responsive, animation are pure HTML - CSS3. 


Quick start
-----------

1. Add "gondola" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'gondola',
    ]

2. Include the gondola URLconf in your project urls.py like this::

    url(r'^gondola/', include('gondola.urls', namespace='gondola')),

3. Run `python manage.py migrate` to create the gondola models.

4. Start the development server and visit http://127.0.0.1:8000/. You should
   click on 'load demo data' to see how it looks like.


Requirements
------------

Pay attention that Gondola requires 'django-tables2' to be installed and
configured.


How to use
----------

In a template load the gondola template tag library then you will be  able
to use the template tag 'gondola'.

.. code:: python
    {% load gondola %}

    ...

    {% gondola %}

To manage gondole, create new row, add new images, visit the
``gondola/dashboard`` page.



.. code:: python

    ``virtualenv -p /usr/bin/python3 gondola``

    ``pip install -r requirements/development.txt``

    ``./manage.py migrate``

    `./manage.py runserver`


If you want to test the app with fake data you can instead see the
django-gondola-sandbox instead.



