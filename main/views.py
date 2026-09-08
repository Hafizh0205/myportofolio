from django.shortcuts import render
from main.models import Experience

def show_main(request):
    context = {
        "name": "Hafizh Zuhdi Hartanto",
        "npm": "2506656785",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada cloud computing, backend infrastructure, dan digital systems."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Hafizh Zuhdi Hartanto",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)