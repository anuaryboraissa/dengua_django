import os
import environ

environ.Env.read_env()

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secure.settings')

application = get_wsgi_application()