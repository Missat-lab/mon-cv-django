from django.shortcuts import render, get_object_or_404
from .models import Person

def home(request):
    person = Person.objects.first()
    return render(request, "core/home.html", {"person": person})
