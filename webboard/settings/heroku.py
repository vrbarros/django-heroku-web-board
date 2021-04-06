# flake8: noqa

import django_heroku

from .base import *

# Activate Django-Heroku
# https://devcenter.heroku.com/articles/django-app-configuration

django_heroku.settings(locals())
