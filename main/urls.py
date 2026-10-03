from django.urls import path
from main.views import (
    show_main, 
    show_experience, 
    create_experience,
    create_experience_ajax,
    edit_experience,
    delete_experience,
    toggle_star_experience,
    get_experience_json,
    get_experience_json_by_id,
    show_projects, 
    create_project,
    create_project_ajax, 
    get_projects_json,
    delete_project,
    toggle_star,  
    register,     
    login_user,   
    logout_user   
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),

    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("experience/edit/<int:id>/", edit_experience, name="edit_experience"),
    path("experience/delete/<int:id>/", delete_experience, name="delete_experience"),
    path("experience/<int:id>/star/", toggle_star_experience, name="toggle_star_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("api/experience/<int:id>/", get_experience_json_by_id, name="get_experience_json_by_id"),

    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"), 
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
]