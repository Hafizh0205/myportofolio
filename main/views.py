def show_experience(request):
    if not Experience.objects.exists():
        Experience.objects.create(
            title="Staff Departemen Olahraga BEM Fasilkom UI",
            description="Penanggung Jawab (PJ) UKOR Tenis Lapangan dan PJ Kontingen CSUI untuk ajang Olimpiade UI.",
            category="organization"
        )
        
    experience_list = Experience.objects.all()
    context = {
        'experience_list': experience_list,
    }
    return render(request, 'experience.html', context)