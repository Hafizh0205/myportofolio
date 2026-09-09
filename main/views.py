from django.shortcuts import render
from main.models import Experience

def show_main(request):
    context = {
        'name': 'Hafizh Zuhdi Hartanto',
        'npm': '2506656785',
        'study_program': 'S1 Ilmu Komputer',
        'bio': 'Undergraduate Computer Science student at Fasilkom UI, passionate about technology, operating systems, and software engineering.',
    }
    return render(request, 'index.html', context)

def show_experience(request):
    if not Experience.objects.exists():
        Experience.objects.create(
            title="Staff Departemen Olahraga BEM Fasilkom UI",
            description="PJ UKOR Tenis Lapangan dan PJ Kontingen CSUI untuk ajang Olimpiade UI.",
            category="organization"
        )

    experience_list = Experience.objects.all()
    context = {
        'experience_list': experience_list,
    }
    return render(request, 'experience.html', context)