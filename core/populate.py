from core.models import Person, Experience, Competence, Formation

# Supprimer les anciennes données (optionnel pour test)
Person.objects.all().delete()

# Créer la personne
ramadan = Person.objects.create(
    prenom="Ramadan Karim",
    nom="DiwenikaMissat",
    titre="Élève ingénieur en système et réseau informatique",
    email="diwenikamissat@gmail.com",
    telephone="72104143",
    ville="Bangui, Central African Republic",
    linkedin="https://www.linkedin.com/in/ramadan-karim-data",
    resume_text="Information management Assistant - résumé et summary ici..."
)

# Compétences
Competence.objects.bulk_create([
    Competence(person=ramadan, nom="Solar System Design", niveau=90),
    Competence(person=ramadan, nom="Battery configurations and Inverter Setup", niveau=85),
    Competence(person=ramadan, nom="Phase I Environmental Site Assessments", niveau=80),
])

# Expériences
Experience.objects.bulk_create([
    Experience(
        person=ramadan,
        titre="Information Management Assistant",
        organisation="MINUSCA",
        date_debut="August 2024",
        date_fin="Present",
        description="""Collecte, organisation et analyse des données pour soutenir la prise de décision au sein de l'équipe de planification. Utilisation de Power BI, Power Apps, Excel, Power Query, SharePoint, UMOJA et CPAS.""",
        ordre=1
    ),
    Experience(
        person=ramadan,
        titre="Logistics Planning Manager & Executive Assistant",
        organisation="Société NDOL-CITY SURL",
        date_debut="December 2017",
        date_fin="August 2024",
        description="Gestion des opérations logistiques et support exécutif. Optimisation des inventaires, coordination fournisseurs, reporting financier et suivi administratif.",
        ordre=2
    ),
    Experience(
        person=ramadan,
        titre="Solar Energy Technician & Installer",
        organisation="Self-employed",
        date_debut="April 2023",
        date_fin="May 2024",
        description="Installation de systèmes solaires off-grid pour entreprises et résidences.",
        ordre=3
    ),
])

# Formations
Formation.objects.bulk_create([
    Formation(person=ramadan, diplome="DUT, Génie informatique", ecole="Institut Polytechnique Universitaire et Professionnel", date_debut="Septembre 2014", date_fin="Juillet 2016"),
    Formation(person=ramadan, diplome="Certificat professionnel, Logistique et approvisionnement", ecole="The Chartered Institute of Logistics and Transport UK", date_debut="Juin 2022", date_fin="Octobre 2023"),
    Formation(person=ramadan, diplome="Bachelor's degree, Computer Systems Networking and Telecommunications", ecole="MIT University of Dakar", date_debut="Avril 2025", date_fin="Novembre 2025"),
])
