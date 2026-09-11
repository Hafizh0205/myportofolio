from django.shortcuts import render
from main.models import Experience, Education

def show_main(request):
    context = {
        'name': 'Hafizh Zuhdi Hartanto',
        'npm': '2506656785',
        'study_program': 'S1 Ilmu Komputer',
        'bio': 'Undergraduate Computer Science student at Fasilkom UI, passionate about technology, operating systems, and software engineering.',
    }
    return render(request, 'index.html', context)

def show_experience(request):
    experience_list = Experience.objects.all()
    context = {
        'experience_list': experience_list,
    }
    return render(request, 'experience.html', context)

def show_education(request):
    education_list = Education.objects.all()
    context = {
        'education_list': education_list,
    }
    return render(request, 'education.html', context)