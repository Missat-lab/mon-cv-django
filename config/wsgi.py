import os
from django.core.wsgi import get_wsgi_application

# Définit le settings module si non défini dans l'environnement
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
