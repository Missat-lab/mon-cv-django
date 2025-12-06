import os
from django.core.asgi import get_asgi_application

# Définit le settings module si non défini dans l'environnement
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_asgi_application()
