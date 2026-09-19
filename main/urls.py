from django.urls import path
from main.views import (
    show_main, 
    show_experience, 
    create_experience,
    edit_experience,
    delete_experience,
    get_experience_json,
    get_experience_json_by_id,
    show_projects, 
    create_project,
    get_projects_json,
    delete_project
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    
    # --- ROUTE EXPERIENCE ---
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/edit/<int:id>/", edit_experience, name="edit_experience"),
    path("experience/delete/<int:id>/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("api/experience/<int:id>/", get_experience_json_by_id, name="get_experience_json_by_id"),

    # --- ROUTE PROJECTS ---
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"), # Menggunakan uuid
]