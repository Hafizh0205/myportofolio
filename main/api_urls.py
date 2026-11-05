from django.urls import path
from main import api_views

app_name = "api"

urlpatterns = [
    # Tutorial 07 (Project)
    path("projects/", api_views.project_list, name="project-list"),
    path("projects/<uuid:project_id>/", api_views.project_detail, name="project-detail"),
    path("projects/<uuid:project_id>/star/", api_views.project_star, name="project-star"),

    # Tugas 6 (Experience)
    path("experience/", api_views.experience_list, name="experience-list"),
    path("experience/<int:id>/", api_views.experience_detail, name="experience-detail"),
    path("experience/<int:id>/star/", api_views.experience_star, name="experience-star"),
]