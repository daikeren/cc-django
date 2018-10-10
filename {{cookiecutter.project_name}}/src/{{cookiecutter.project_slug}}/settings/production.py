from .base import *       # NOQA

DEBUG = env.bool('DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = env('SECRET_KEY', default='SECRET_KEY')

CACHES = {
    'default': env.cache_url('CACHE_URL', default='locmemcache://'),
}

EMAIL_CONFIG = env.email_url(
    'EMAIL_URL', default='consolemail://'
)

vars().update(EMAIL_CONFIG)

MIDDLEWARE = [
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware'
] + MIDDLEWARE
ALLOWED_HOSTS = str(env('ALLOWED_HOSTS')).split(',')
