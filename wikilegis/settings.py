"""
Django settings for wikilegis project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Import `default` as the default settings. This can be handy while pushing items into tuples.
import django.conf.global_settings as default


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

from wikilegis import confutils

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'g8#!8*0sr!zsg!q=on=n66dtie69u0z1qhfk-&c8bc_%t#&g@%')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = confutils.environ_to_boolean(os.environ.get('DEBUG'))

ALLOWED_HOSTS = confutils.environ_to_list_of_strings(os.environ.get('ALLOWED_HOSTS'))


# Application definition

INSTALLED_APPS = (
    'wikilegis.auth2',
    'wikilegis.core',
    'wikilegis.helpers',
    'wikilegis.comments2',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    'haystack',
    'compressor',
    'adminsortable2',
    'debug_toolbar',
    'registration',
    'django_comments',
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'wikilegis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wikilegis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

import dj_database_url
DATABASES = dict(default=dj_database_url.config())

try:
    import django_postgrespool
except ImportError:
    pass
else:
    DATABASES['default']['ENGINE'] = 'django_postgrespool'


# django-haystack: http://django-haystack.readthedocs.org/
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}


# Authentication and user management

AUTH_USER_MODEL = 'auth2.User'

# If `False` the registration view will not require user activation through e-mail.
# Useful to disable activation during DEBUG or other situations where mails can't be sent.
ACCOUNT_ACTIVATION_REQUIRED = not DEBUG

ACCOUNT_ACTIVATION_DAYS = 7

REGISTRATION_AUTO_LOGIN = True

REGISTRATION_FORM = 'wikilegis.auth2.forms.RegistrationForm'

# XXX Please don't change. The URL is included in `wikilegis.auth2.urls`.
INCLUDE_REGISTER_URL = False

LOGIN_REDIRECT_URL = '/'


# Use GMail SMTP to send mail.

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = 587

# django.contrib.sites: https://docs.djangoproject.com/en/1.8/ref/contrib/sites/

SITE_ID = 1


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = os.environ.get('DJANGO_LANGUAGE_CODE', 'en')

TIME_ZONE = os.environ.get('TZ', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'public'))


# django-compressor: http://django-compressor.readthedocs.org/

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_OFFLINE = confutils.environ_to_boolean(os.environ.get('COMPRESS_OFFLINE')) or not DEBUG

STATICFILES_FINDERS = default.STATICFILES_FINDERS + (
    'compressor.finders.CompressorFinder',
)

# whitenoise: http://whitenoise.evans.io/en/latest/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# Whether we want to serve static files or not.

SERVE_STATIC_FILES = confutils.environ_to_boolean(os.environ.get('SERVE_STATIC_FILES')) or DEBUG


# django-debug-toolbar: http://django-debug-toolbar.readthedocs.org/
STATIC_IPS = ('127.0.0.1', '::1', )


# logging:
# Log everything we can to stdout. It's the Heroku way.

import sys
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'filters': [],
            'propagate': True,
            'level': 'DEBUG',
        },
    },
    'root': {
        'handlers': ['console', ],
        'level': 'INFO'
    },
}


