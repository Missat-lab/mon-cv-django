from django.shortcuts import render
from django.db.models import Prefetch
from .models import Person, Experience, Competence, Formation, Project, Language, Interest

def home(request):
    person = (
        Person.objects
        .prefetch_related(
            Prefetch("experiences", queryset=Experience.objects.order_by("-ordre")),
            Prefetch("competences", queryset=Competence.objects.order_by("-niveau")),
            Prefetch("formations", queryset=Formation.objects.order_by("-date_debut")),
            Prefetch("projects"),
            Prefetch("languages"),
            Prefetch("interests"),
        )
        .first()
    )

    if not person:
        return render(request, "core/home.html", {"message": "Aucun CV disponible pour le moment."})

    context = {
        "person": person,
        "experiences": person.experiences.all(),
        "competences": person.competences.all(),
        "formations": person.formations.all(),
        "projects": person.projects.all(),
        "languages": person.languages.all(),
        "interests": person.interests.all(),
    }
    return render(request, "core/home.html", context)
