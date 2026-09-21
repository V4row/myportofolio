from django.urls import path

from main.views import (
    show_main,
    show_experience,
    show_skill,
    show_project,
    create_project,
    update_project,
    delete_project,
    get_project_json,
    create_experience,
    get_experience_json,
    delete_experience,
    update_experience,
    )

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("skill/", show_skill, name="show_skill"),
    path("project/", show_project, name="show_project"),
    path("project/add/", create_project, name="create_project"),
    path("api/project/", get_project_json, name="get_project_json"),
    path("project/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("experience/add/", create_experience, name="create_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("project/<uuid:project_id>/update/", update_project, name="update_project"),
    path("experience/<uuid:experience_id>/update/", update_experience, name="update_experience"),
]