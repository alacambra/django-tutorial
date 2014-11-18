__author__ = 'alacambra'

from TaskManager.models import Project
from django.shortcuts import render


def create(request):
    project = Project()
    project.title = "Task manager with Django"
    project.description = "Starting with django smoothly"
    project.save()
    return render(request, 'en/public/project.html')


def page(request):
    projects = Project.objects.all().get()
    return render(request, 'en/public/project.html', {"projects": projects})