"""
Django settings for villagalde project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os import path, pardir
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zd5!qir%u#gr9q1t17dki_*mf+jl^#(*urtvq5!1dgi9k1q6k%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taggit',
    'villagalde.apps.blog',
    'jquery',
    'suit_ckeditor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'villagalde.urls'

WSGI_APPLICATION = 'villagalde.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'villagalde',
        'USER': 'villagalde',
        'PASSWORD': 'jfjejudbfvik',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',
        'OPTIONS'  : { 'init_command' : 'SET storage_engine=MyISAM', },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = 'http://leafar07j.posnclouds.com/static/'


# STATIC_URL = '/srv/www/villagalde/villagalde/villagalde/static/'

STATIC_ROOT = os.path.join('/srv/www/villagalde/villagalde/static/')

# Additional locations of static files
STATICFILES_DIRS = (
   os.path.join(PROJECT_ROOT,'static'),

)

MEDIA_ROOT = '/srv/www/villagalde/villagalde/villagalde/media/'

MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
   #os.path.join(PROJECT_ROOT,'templates'),
   os.path.join(os.path.dirname(__file__),'templates'),

)

