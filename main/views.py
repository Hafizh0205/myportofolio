from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from main.models import Experience, Project
from main.forms import ProjectForm

def show_main(request):
    return render(request, 'index.html')

def show_experience(request):
    experience_list = Experience.objects.all()
    context = {'experience_list': experience_list}
    return render(request, 'experience.html', context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)
    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def show_projects(request):
    json_response = get_projects_json(request)
    projects_deserialized = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8")
    )
    projects = [p.object for p in projects_deserialized]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Hafizh Zuhdi Hartanto",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")
    
    context = {
        "name": "Hafizh Zuhdi Hartanto",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
    return redirect("main:show_projects")