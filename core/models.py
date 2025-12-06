from django.db import models

class Person(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    titre = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=50, blank=True)
    ville = models.CharField(max_length=100, blank=True)
    linkedin = models.URLField(blank=True)
    resume_text = models.TextField(blank=True)  # résumé / summary

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Experience(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="experiences")
    titre = models.CharField(max_length=255)
    organisation = models.CharField(max_length=255)
    date_debut = models.CharField(max_length=50, blank=True)  # text-friendly (ex: August 2024)
    date_fin = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    ordre = models.IntegerField(default=0)

    class Meta:
        ordering = ["-ordre"]

    def __str__(self):
        return f"{self.titre} @ {self.organisation}"


class Competence(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="competences")
    nom = models.CharField(max_length=200)
    niveau = models.IntegerField(default=80)  # pour barres de compétences

    def __str__(self):
        return self.nom


class Formation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="formations")
    ecole = models.CharField(max_length=255)
    diplome = models.CharField(max_length=255)
    date_debut = models.CharField(max_length=50, blank=True)
    date_fin = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.diplome} — {self.ecole}"
