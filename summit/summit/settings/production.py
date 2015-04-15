from .base import *

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['summit.pywaw.org']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_var('DB_NAME'),
        'USER': get_env_var('DB_USER'),
        'PASSWORD': get_env_var('DB_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
MANDRILL_API_KEY = get_env_var('MANDRILL_API_KEY')
REGISTRATION_NOTIFICATIONS_URL = get_env_var('REGISTRATION_NOTIFICATIONS_URL', default=None)

TWITTER_CONSUMER_KEY=get_env_var("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET=get_env_var("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN=get_env_var("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET=get_env_var("TWITTER_ACCESS_TOKEN_SECRET")
