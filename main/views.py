from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from main.models import Experience, Project
from main.forms import ProjectForm, ExperienceForm

def show_main(request):
    return render(request, 'index.html')

# ========================================================
# SECTION PROJECTS (TUTORIAL 03)
# ========================================================

def show_projects(request):
    json_response = get_projects_json(request)
    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8")
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Hafizh Zuhdi Hartanto",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)
    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

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
    return redirect("main:show_projects")


# ========================================================
# SECTION EXPERIENCE (TUGAS 3)
# ========================================================

# 1. Menampilkan Experience via JSON Deserialization
def show_experience(request):
    json_response = get_experience_json(request)
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8")
    )
    experiences = [exp.object for exp in experiences]

    context = {
        "name": "Hafizh Zuhdi Hartanto",
        "experience_list": experiences,
    }
    return render(request, "experience.html", context)

# 2. Endpoint JSON Delivery untuk Experience
def get_experience_json(request):
    experiences = Experience.objects.all()
    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def get_experience_json_by_id(request, id):
    experience = Experience.objects.filter(pk=id)
    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")

# 3. Create Experience
def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Hafizh Zuhdi Hartanto",
        "form": form,
    }
    return render(request, "experience_form.html", context)

# 4. Update Experience (Edit Data berdasarkan ID)
def edit_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Hafizh Zuhdi Hartanto",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)

# 5. Delete Experience
def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")
    return redirect("main:show_experience")