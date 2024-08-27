import os
from .base import *
import environ
 # Allow your site to be included in browsers' HSTS preload lists
env = environ.Env()
environ.Env.read_env()
DEBUG = False
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSP_DEFAULT_SRC = ("'self'",)
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
ALLOWED_HOSTS = ["*"]
SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = 'DENY'
# settings.py
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include subdomains if applicable
SECURE_HSTS_PRELOAD = True 
DATABASES = {
    'default': {
        'ENGINE': env('SQL_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env('SQL_DATABASE', default=os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': env('SQL_USER', default='user'),
        'PASSWORD': env('SQL_PASSWORD', default='password'),
        'HOST': env('SQL_HOST', default='localhost'),
        'PORT': env('SQL_PORT', default=''),
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_AGE = 1209600 

# settings.py
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': '/path/to/django/debug.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }

