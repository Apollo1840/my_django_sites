"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

application = get_wsgi_application()

sys.path.append('/home/congyu/congyu_program/react/my_django_sites/CommunityBlogs')
sys.path.append('/home/congyu/congyu_program/react/my_django_sites/CommunityBlogs/django_project')

import logging

logging.basicConfig(stream=sys.stderr)
logging.getLogger().setLevel(logging.DEBUG)

logging.debug('Python executable: %s', sys.executable)
logging.debug('sys.path: %s', sys.path)
