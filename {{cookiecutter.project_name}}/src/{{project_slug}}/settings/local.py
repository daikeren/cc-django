from .base import *       # NOQA

DEBUG = env.bool('DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = env('SECRET_KEY', default='SECRET_KEY')
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INSTALLED_APPS += [
    'debug_toolbar',
]

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

CELERY_ALWAYS_EAGER = True
ALLOWED_HOSTS = [
    '*',
]

