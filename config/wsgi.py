import os
from django.core.wsgi import get_wsgi_application

# Remplace TONPROJET par le nom du dossier où se trouvent settings.py, urls.py, asgi.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configs.settings")

application = get_wsgi_application()
