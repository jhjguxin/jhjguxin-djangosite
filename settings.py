#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Django settings for mysite project.
import os
DEBUG = True#True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
      ('wwew', '905455194@qq.com'),
      ('孤心', '864248765@qq.com'),
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS
#MANAGERS = (
#    ('George Harrison', 'gharrison@example.com'),
#    ('Ringo Starr', 'ringo@example.com'),
#)

DATABASES = {
    'default': {
        'ENGINE': 'mysql',
                  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME':'mysql',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'jhjwwew12315123',                  # Not used with sqlite3.
        'HOST': '/var/run/mysqld/mysqld.sock',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
#TIME_ZONE = 'America/Chicago'
TIME_ZONE = 'Asia/Chongqing'
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
#ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

MEDIA_ROOT = '/usr/lib/pymodules/python2.7/django/contrib/admin/media/'
#MEDIA_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"

MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX ="/media/"

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$0wjfm245w-a0fm1n$yiir0$hs@j$3ywoy97wgmyx+!!6x78no'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.Loader',
)
#request是顺序执行的响应中间件是自后向前执行的
MIDDLEWARE_CLASSES = (
     'django.middleware.common.CommonMiddleware',
     'django.contrib.sessions.middleware.SessionMiddleware',
     'django.middleware.locale.LocaleMiddleware',            
     'django.contrib.auth.middleware.AuthenticationMiddleware',
     #"django.contrib.auth.context_processors.auth",
      "django.middleware.csrf.CsrfMiddleware",
      "django.middleware.csrf.CsrfViewMiddleware",
      "django.middleware.csrf.CsrfResponseMiddleware",
      'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware', 
      "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
      "django.middleware.gzip.GZipMiddleware",
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATE_DIRS = (
    "/home/jhjguxin/Desktop/djcode/mysite/templates",
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.sites',
#    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
      'south',
      'mysite.books',
      'mysite.books.templatetags',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.sitemaps',
      'django.contrib.sites',
      'django.contrib.redirects',
      'django.contrib.flatpages',
)
#默认登录地址LOGIN_URL (/accounts/login/ by default)
LOGIN_URL='/login'
