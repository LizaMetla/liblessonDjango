"""
Django settings for liblesson project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import logging
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from core.utils.logs import DebugInfoFilter

BASE_DIR = Path(__file__).resolve().parent.parent
VERSION = '0.1.2.0'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-eo1em6ap5#-u5r*aibi(5ruzr-xz@=mhsb8##l1srd4^6-rza_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middlewares.auth.VisitCountMiddleware',
    'core.middlewares.auth.VersionMiddleware'

]

ROOT_URLCONF = 'liblesson.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'liblesson.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'postgres',
        'PORT': 5432,
    },

}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOG_FOLDER = os.path.join(BASE_DIR, 'logs')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'debug-info-filter': {
            '()': DebugInfoFilter,
            'param': 'noshow',
        }
    },
    'handlers': {
        'file-handler':
            {
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOG_FOLDER, 'console.log'),
                'filters': ['debug-info-filter']
            },
        'auth-file-handler':
            {
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOG_FOLDER, 'auth.txt'),
            },
        'db-handler':
            {
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOG_FOLDER, 'db.txt'),
            },
        'file-errors-handler':
            {
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOG_FOLDER, 'console.errors.log'),
                'level': 'ERROR'
            },
        'actions-handler':
            {
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOG_FOLDER, 'actions.logs'),
            },
        'registrations-handler':
            {
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOG_FOLDER, 'registrations.logs')
            }
    },
    'loggers': {
        'django': {
            'handlers': ['file-handler', 'file-errors-handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'auth': {
            'handlers': ['auth-file-handler'],
            'propagate': False,
            'level': 'INFO',
        },
        'django.db.backends': {
            'handlers': ['db-handler'],
            'propagate': False,
            'level': 'INFO',
        },
        'actions': {
            'handlers': ['actions-handler'],
            'propagate': False,
            'level': 'INFO',
        },
        'registrations': {
            'handlers': ['registrations-handler'],
            'propagate': False,
            'level': 'INFO',
        }
    },
}