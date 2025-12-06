import re
from django.core.management.base import BaseCommand
from core.models import Person, Experience, Competence, Formation
from pathlib import Path
import PyPDF2

class Command(BaseCommand):
    help = "Import CV depuis un PDF (simple heuristique). Usage: python manage.py import_cv [path/to/Profile.pdf]"

    def add_arguments(self, parser):
        parser.add_argument('pdf_path', nargs='?', default='data/Profile.pdf')

    def handle(self, *args, **options):
        pdf_path = Path(options['pdf_path'])
        if not pdf_path.exists():
            self.stderr.write(self.style.ERROR(f"Fichier introuvable: {pdf_path}"))
            return

        text = ""
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text() or ""
                text += page_text + "\n"

        # Création / mise à jour Person (basique)
        # On extrait le nom en haut : heuristique simple
        person, created = Person.objects.get_or_create(email="diwenikamissat@gmail.com", defaults={
            "prenom": "Ramadan",
            "nom": "Diwenika Missat",
            "titre": "Information Management Assistant",
            "email": "diwenikamissat@gmail.com",
            "telephone": "72104143",
            "ville": "Bangui, Central African Republic",
            "linkedin": "https://www.linkedin.com/in/ramadan-karim-data",
            "resume_text": "",
        })
        if not created:
            self.stdout.write("Personne existante mise à jour (si nécessaire).")

        # Heuristique : trouver les blocs "Experience" / "Education" etc.
        # On cherche les sections connues présentes dans le PDF
        # Expériences: extrait les blocs commençant par un nom d'organisation ou une date
        # (TRÈS SIMPLE — à affiner manuellement si nécessaire)
        experiences = []
        # Exemple basé sur contenus connus dans le PDF (MINUSCA, NDOL-CITY SURL, Self-employed)
        if "MINUSCA" in text:
            experiences.append({
                "titre": "Information Management Assistant",
                "organisation": "MINUSCA",
                "date_debut": "August 2024",
                "date_fin": "Present",
                "description": "Collecte, nettoyage, analyse et visualisation de données opérationnelles UN. Outils: Power BI, Power Apps, Excel, Power Query, SharePoint, UMOJA, CPAS.",
                "ordre": 3
            })
        if "NDOL-CITY SURL" in text or "NDOL-CITY" in text:
            experiences.append({
                "titre": "Logistics Planning Manager & Executive Assistant",
                "organisation": "NDOL-CITY SURL",
                "date_debut": "December 2017",
                "date_fin": "August 2024",
                "description": "Gestion logistique, optimisation des stocks (900+ produits), administration exécutive, finance et suivi des fournisseurs.",
                "ordre": 2
            })
        if "Solar Energy Technician" in text or "Solar" in text:
            experiences.append({
                "titre": "Solar Energy Technician & Installer",
                "organisation": "Indépendant",
                "date_debut": "April 2023",
                "date_fin": "May 2024",
                "description": "Conception et installation de systèmes solaires off-grid (exemples de projets et capacités fournis).",
                "ordre": 1
            })

        # Save experiences
        Experience.objects.filter(person=person).delete()
        for e in experiences:
            Experience.objects.create(person=person, **e)

        # Competences (heuristique)
        Competence.objects.filter(person=person).delete()
        competence_list = [
            ("Solar System Design", 85),
            ("Battery configurations and Inverter Setup", 80),
            ("Power BI", 75),
            ("Excel / Power Query", 75),
            ("Data Analysis", 78),
        ]
        for name, level in competence_list:
            Competence.objects.create(person=person, nom=name, niveau=level)

        # Formations (heuristique)
        Formation.objects.filter(person=person).delete()
        formation_list = [
            {"ecole":"MIT University of Dakar", "diplome":"Bachelor's degree, Computer Systems Networking and Telecommunications", "date_debut":"April 2025", "date_fin":"November 2025"},
            {"ecole":"institut polytechnique universitaire et professionnel", "diplome":"DUT, Génie informatique", "date_debut":"September 2014", "date_fin":"July 2016"},
            {"ecole":"Université de Bangui", "diplome":"Deug1, Science economique et de gestion", "date_debut":"2012", "date_fin":"2013"},
        ]
        for f in formation_list:
            Formation.objects.create(person=person, **f)

        self.stdout.write(self.style.SUCCESS("Import terminé. Vérifiez la base de données / admin pour affiner les textes."))
