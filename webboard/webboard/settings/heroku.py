import django_heroku
import os

from .base import *

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Activate Django-Heroku
# https://devcenter.heroku.com/articles/django-app-configuration

django_heroku.settings(locals())
