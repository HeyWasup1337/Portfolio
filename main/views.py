from django.shortcuts import render
from .models import Project, Skill

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'main/home.html', context)