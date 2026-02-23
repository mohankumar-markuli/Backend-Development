"""
ASGI - Asynchronous Server Gateway Interface - is a specification that describes 
how an asynchronous web server communicates with asynchronous web applications. 
It allows for a standardized way to deploy and runPython web applications 
that can handle asynchronous tasks, including those built with Django.

ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_asgi_application()
