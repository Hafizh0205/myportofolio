from django.shortcuts import render
from main.models import Experience, Project

def show_main(request):
    return render(request, 'index.html')

def show_experience(request):
    experience_list = Experience.objects.all()
    context = {'experience_list': experience_list}
    return render(request, 'experience.html', context)

def show_projects(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'projects.html', context)