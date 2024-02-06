from .base import *
import os

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'static'))]
