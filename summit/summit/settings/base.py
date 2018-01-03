"""
Django settings for summit project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
from django.core.exceptions import ImproperlyConfigured


def get_env_var(name, **kwargs):
    try:
        return os.environ[name]
    except KeyError:
        if 'default' in kwargs:
            return kwargs['default']
        raise ImproperlyConfigured('Set the {} environment variable.'.format(name))


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_var('SECRET_KEY', default='secret')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'djrill',
    'registration',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'summit.urls'

WSGI_APPLICATION = 'summit.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/2015/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATIC_ROOT = '/static'
MEDIA_ROOT = '/media'

SASS_BIN = '/usr/local/bin/node-sass'

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', SASS_BIN + ' {infile} --stdout --include-path static/bower_components/'),
)

REGISTRATION_EMAIL = 'Registration <registration@pywaw.org>'
REGISTRATION_NOTIFICATIONS_URL = None
