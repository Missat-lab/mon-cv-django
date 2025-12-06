from django.contrib import admin
from .models import Person, Experience, Competence, Formation, Project, Language, Interest

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 0

class CompetenceInline(admin.TabularInline):
    model = Competence
    extra = 0

class FormationInline(admin.TabularInline):
    model = Formation
    extra = 0

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 0

class LanguageInline(admin.TabularInline):
    model = Language
    extra = 0

class InterestInline(admin.TabularInline):
    model = Interest
    extra = 0

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [ExperienceInline, CompetenceInline, FormationInline, ProjectInline, LanguageInline, InterestInline]
    list_display = ("prenom", "nom", "titre", "email")
    search_fields = ("prenom", "nom", "email", "titre")
    list_filter = ("titre",)
