from core.models import Person, Competence, Experience, Formation, Project, Language, Interest

# Attention : supprimez les existants si nécessaire
Person.objects.all().delete()

ramadan = Person.objects.create(
    prenom="Ramadan Karim",
    nom="Diwenika Missat",
    titre="Élève ingénieur en système et réseau informatique",
    email="diwenikamissat@gmail.com",
    telephone="72104143",
    ville="Bangui",
    pays="Central African Republic",
    linkedin="https://www.linkedin.com/in/ramadan-karim-data",
    github="",
    resume_text=(
        "Information management Assistant - Collecte, organisation et analyse des données "
        "pour soutenir la prise de décision. Compétences : Power BI, Power Apps, Excel, Power Query, SharePoint."
    ),
)

# Nouvelles compétences principales (Python, SQL, Power BI, etc.)
competences_data = [
    {"nom": "Python (Jupyter Notebook, Google Colab)", "niveau": 90},
    {"nom": "Statistique appliquée avec Excel", "niveau": 85},
    {"nom": "SQL (Oracle DB, PostgreSQL)", "niveau": 85},
    {"nom": "Excel avancé & Power Query", "niveau": 95},
    {"nom": "Power BI & Power Platform", "niveau": 90},
    {"nom": "QlikSense", "niveau": 85},
    {"nom": "SharePoint", "niveau": 80},
    {"nom": "CPAS (Corporate Planning and Analysis System)", "niveau": 80},
    {"nom": "UMOJA (IPMR, SMA)", "niveau": 85},
    {"nom": "UMOJA Self-Service Analytics", "niveau": 80},
    {"nom": "Consolidation, nettoyage et structuration de données", "niveau": 90},
    {"nom": "Création de dashboards et reporting interactif", "niveau": 90},
    {"nom": "Analyse stratégique pour la planification et la prise de décision", "niveau": 85},
]

# Anciennes compétences (à mettre en dernier)
competences_anciennes = [
    {"nom": "Solar System Design", "niveau": 90},
    {"nom": "Battery configurations and Inverter Setup", "niveau": 85},
    {"nom": "Phase I Environmental Site Assessments", "niveau": 80},
]

# Fusion des deux listes (data/IM d'abord, puis autres)
competences = competences_data + competences_anciennes

# Génération du bulk_create
Competence.objects.bulk_create([
    Competence(person=ramadan, nom=c["nom"], niveau=c["niveau"])
    for c in competences
])

Experience.objects.bulk_create([
    Experience(person=ramadan, titre="Information Management Assistant", organisation="MINUSCA",
               date_debut="August 2024", date_fin="Present",
               description="Collecte, organisation et analyse des données.", ordre=1),
    Experience(person=ramadan, titre="Logistics Planning Manager & Executive Assistant", organisation="Société NDOL-CITY SURL",
               date_debut="December 2017", date_fin="August 2024",
               description="Gestion des opérations logistiques et support exécutif.", ordre=2),
    Experience(person=ramadan, titre="Solar Energy Technician & Installer", organisation="Self-employed",
               date_debut="April 2023", date_fin="May 2024",
               description="Installation de systèmes solaires off-grid.", ordre=3),
])

Formation.objects.bulk_create([
    Formation(person=ramadan, diplome="DUT, Génie informatique", ecole="Institut Polytechnique Universitaire et Professionnel",
              date_debut="Septembre 2014", date_fin="Juillet 2016"),
    Formation(person=ramadan, diplome="Certificat professionnel, Logistique et approvisionnement",
              ecole="The Chartered Institute of Logistics and Transport UK", date_debut="Juin 2022", date_fin="Octobre 2023"),
    Formation(person=ramadan, diplome="Bachelor's degree, Computer Systems Networking and Telecommunications",
              ecole="MIT University of Dakar", date_debut="Avril 2025", date_fin="Novembre 2025"),
])

Project.objects.bulk_create([
    Project(person=ramadan, title="Installation Solaire Off-grid", description="Projet d'installation solaire pour PME.", link=""),
])

Language.objects.bulk_create([
    Language(person=ramadan, name="Français", level="Natif"),
    Language(person=ramadan, name="Anglais", level="Courant"),
])

Interest.objects.bulk_create([
    Interest(person=ramadan, name="Technologie"),
    Interest(person=ramadan, name="Énergies renouvelables"),
])

print("✅ Données insérées.")
