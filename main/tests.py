from django.test import TestCase, Client
from main.models import Experience

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'index.html')

    def test_experience_url_is_exist(self):
        response = self.client.get('/experience/')
        self.assertEqual(response.status_code, 200)

    def test_experience_using_experience_template(self):
        response = self.client.get('/experience/')
        self.assertTemplateUsed(response, 'experience.html')

    def test_experience_creation(self):
        exp = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami dasar pengembangan web.",
            category="part-time"
        )
        self.assertEqual(exp.title, "Asisten Dosen PBP")
        self.assertTrue(exp.is_ongoing)