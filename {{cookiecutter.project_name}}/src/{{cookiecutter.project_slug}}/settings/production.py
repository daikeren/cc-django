from .base import *       # NOQA

DEBUG = env.bool('DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = env('SECRET_KEY', default='SECRET_KEY')

CACHES = env.cache()
EMAIL_CONFIG = env.email_url(
    'EMAIL_URL', default='consolemail://')

vars().update(EMAIL_CONFIG)

MIDDLEWARE = [
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware'
] + MIDDLEWARE
