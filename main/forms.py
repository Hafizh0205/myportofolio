from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput
from main.models import Project, Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "tech_stack", "project_url", "project_image_url"]
        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }
        widgets = {
            "title": TextInput(attrs={"placeholder": "Portfolio Website", "maxlength": 255}),
            "description": Textarea(attrs={"placeholder": "Ceritakan Proyekmu", "rows": 3}),
            "tech_stack": TextInput(attrs={"placeholder": "Django, Python, HTML, CSS"}),
            "project_url": URLInput(attrs={"placeholder": "https://github.com/Hafizh0205/myportofolio"}),
            "project_image_url": URLInput(attrs={"placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000"}),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "category", "description", "ended_at"]
        labels = {
            "title": "Judul Pengalaman / Posisi",
            "category": "Kategori / Organisasi",
            "description": "Deskripsi Pengalaman",
            "ended_at": "Tanggal Selesai (Kosongkan jika masih berlangsung)",
        }
        widgets = {
            "title": TextInput(attrs={"placeholder": "Staff Departemen Olahraga"}),
            "category": TextInput(attrs={"placeholder": "BEM Fasilkom UI"}),
            "description": Textarea(attrs={"placeholder": "Ceritakan peran dan kontribusimu...", "rows": 3}),
            "ended_at": DateInput(attrs={"type": "date"}),
        }