"""
Django settings for DjangoOnlineShop project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from pathlib import Path

from django.utils import timezone

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3zz^@6himy_%g1l5(ooqnmm@cml2ocyehiob#6f53&!0bjil3y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

if DEBUG:
    INTERNAL_IPS = [
        "127.0.0.1",
    ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    "home.apps.HomeConfig",
    "accounts.apps.AccountConfig",
    'orders.apps.OrdersConfig',
]

THIRD_PARTY_APPS = [
    'storages',
    'django_celery_beat',
]

DEV_APPS = [
    "debug_toolbar",
]

if DEBUG:
    INSTALLED_APPS += DEV_APPS

INSTALLED_APPS += LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DEV_MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

if DEBUG:
    MIDDLEWARE += DEV_MIDDLEWARE

ROOT_URLCONF = 'DjangoOnlineShop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'orders.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoOnlineShop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_shop",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

# https://docs.djangoproject.com/en/4.2/topics/cache/#redis
# Redis cache

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'accounts.User'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static/'
]

# Media Files
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# OTP
KAVENEGAR_APIKEY = ''

# Login
LOGIN_URL = 'accounts:user_login'

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "accounts.auth.PhoneNumberBackend",
]

# Arvan Bucket Setting
AWS_S3_ACCESS_KEY_ID = '86ba9fdb-e795-46f9-abee-e059f6a4a51e'
AWS_S3_SECRET_ACCESS_KEY = 'e4e5d223821febaea0a6ba24fcd7077b580afb0eb0a7f33d37c45320046787b1'

# Basic Storage configuration for Amazon S3 (Irrespective of Django versions)
AWS_STORAGE_BUCKET_NAME = 'alib-shop'  # - Enter your S3 bucket name HERE
AWS_S3_ENDPOINT_URL = 'https://s3.ir-thr-at1.arvanstorage.ir'
AWS_S3_FILE_OVERWRITE = False
AWS_SERVICE_NAME = 's3'
AWS_LOCAL_STORAGE = f'{BASE_DIR}/aws/'
# Django < 4.2
'''
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
'''

# Django 4.2 >
STORAGES = {
    # Media file (image) management   
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
    },
    # CSS and JS file management
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
    # "staticfiles": {
    #     "BACKEND": "storages.backends.s3.S3Storage",
    # },
}

# Zarinpal confs
MERCHANT = "00000000-0000-0000-0000-000000000000"
SANDBOX = True
