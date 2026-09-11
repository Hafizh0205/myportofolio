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
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title