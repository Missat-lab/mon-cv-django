# CV Web Django

Un site web de CV dynamique, moderne et responsive développé avec **Django** et **Bootstrap 5**.  
Ce projet permet de présenter un CV en ligne avec expériences, éducation, compétences et projets.

---

## 🔹 Fonctionnalités

- Affichage dynamique des expériences et formations depuis la base de données.
- Design responsive et mobile-first grâce à **Bootstrap 5**.
- Gestion facile via l’interface admin de Django.
- Possibilité d’ajouter des projets, compétences ou langues facilement.
- Commande personnalisée pour importer un CV depuis un fichier PDF.

---

## 🛠️ Prérequis

- Python 3.9+
- Django 4+
- pip (gestionnaire de packages Python)
- virtualenv (optionnel mais recommandé)

---

## 💻 Installation

1. **Cloner le dépôt**

```bash
git clone https://github.com/ton-utilisateur/cv-web-django.git
cd cv-web-django

# Mon CV - Django (Bootstrap 5)

Instructions:
1. Créer et activer l'environnement virtuel.
2. Installer les dépendances: `pip install -r requirements.txt`
3. Migrer: `python manage.py migrate`
4. Peupler la base (optionnel): `python manage.py shell` puis `exec(open("core/populate_db.py").read())`
5. Lancer: `python manage.py runserver`
6. Ouvrir: http://127.0.0.1:8000/
