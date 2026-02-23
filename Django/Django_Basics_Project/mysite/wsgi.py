"""
WSGI - Web Server Gateway Interface - is a specification that describes how a web server 
communicates with web applications. It allows for a standardized way to deploy and run
Python web applications, including those built with Django.

WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
