from django.apps import AppConfig

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        try:
            from main.models import Experience
            if not Experience.objects.exists():
                Experience.objects.create(
                    title="Asisten Dosen PBP",
                    description="Membantu mahasiswa memahami dasar pengembangan web.",
                    category="part-time",
                    is_ongoing=True
                )
        except Exception:
            pass