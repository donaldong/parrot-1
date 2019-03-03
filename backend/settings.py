"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#6zwu&dq_5z5s6nkgzwb1nc40863jq4znvx5j)#%+sns_@7&1u'

# SECURITY WARNING: don't run with debug turned on in production!
ENV = os.environ.get('PARROT_ENV', 'development')
DEBUG = ENV not in ('production', 'test')

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',
    'backend.scoreboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # We use WhiteNoise to serve static files (the django-admin site)
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['PARROT_DB_NAME'],
        'USER': os.environ['PARROT_DB_USER'],
        'PASSWORD': os.environ['PARROT_DB_PASSWORD'],
        'HOST': os.environ['PARROT_DB_HOST'],
        'PORT': os.environ['PARROT_DB_PORT'],
    } if ENV == 'production' else {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'regress.db'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

BACKEND_TEMPLATES_DIR = os.path.join(BASE_DIR, 'backend/templates')
STATICFILES_STORAGE = 'backend.static_files_storage.StaticFilesStorage'

if DEBUG:
    # Note the slashes '/.../' are necessary for STATIC_URL
    STATIC_URL = '/frontend/dist/static/'
    FRONTEND_BUILD_DIR = os.path.join(BASE_DIR, 'frontend/dist')
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
        # First locate the built assets. When static files with the same names
        # exist in both directories, the ones from dist will be loaded since
        # they're compiled assets.
        os.path.join(BASE_DIR, 'frontend/dist'),
        os.path.join(BASE_DIR, 'frontend/public'),
    ]
else:
    # Note the slashes '/.../' are necessary for STATIC_URL
    STATIC_URL = '/static/'
    # WhiteNoise needs STATIC_ROOT to serve the static files. Read more at
    #   http://whitenoise.evans.io/en/stable/django.html
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    # Allow the app being hosted on PARROT_HOST to prevent Host Header Attack.
    # If the environment variable is not set, we are in the test environment,
    # so we allow the test server to host the app.
    ALLOWED_HOSTS.append(os.environ.get('PARROT_HOST', 'testserver'))
