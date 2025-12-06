#!/usr/bin/env python3
"""
manage.py

Point d’entrée principal pour toutes les commandes Django.

Exemples d’utilisation :
    python manage.py runserver
    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser
    python manage.py import_cv data/Profile.pdf
"""

import os
import sys
from pathlib import Path

# Vérification de la version Python
if sys.version_info < (3, 9):
    sys.exit("Ce projet nécessite Python 3.9 ou supérieur.")

BASE_DIR = Path(__file__).resolve().parent

def main():
    """Initialise les settings Django et exécute les commandes."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible d'importer Django. Vérifiez que le package est installé "
            "et que votre environnement virtuel est activé."
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
