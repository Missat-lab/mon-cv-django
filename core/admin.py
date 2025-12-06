from django.contrib import admin
from .models import Person, Experience, Competence, Formation

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 0

class CompetenceInline(admin.TabularInline):
    model = Competence
    extra = 0

class FormationInline(admin.TabularInline):
    model = Formation
    extra = 0

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [ExperienceInline, CompetenceInline, FormationInline]
    list_display = ("prenom", "nom", "titre", "email")
