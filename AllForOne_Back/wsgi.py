"""
WSGI config for AllForOne_Back project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling  # For Heroku

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AllForOne_Back.settings')

application = get_wsgi_application()

application = Cling(get_wsgi_application())  # For Heroku
