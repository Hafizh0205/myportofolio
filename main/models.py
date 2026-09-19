import uuid
from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50)
    ended_at = models.DateTimeField(null=True, blank=True)

    @property
    def is_ongoing(self):
        return self.ended_at is None

    def __str__(self):
        return self.title

class Project(models.Model):
    # Menggunakan UUID untuk mencegah error 'id null' di PostgreSQL PWS
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True, null=True)
    project_image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title