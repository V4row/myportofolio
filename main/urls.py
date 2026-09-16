from django.urls import path

from main.views import (
    show_main,
    show_experience,
    show_skill,
    show_project,
    create_project,
    delete_project,
    get_project_json
    )

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("skill/", show_skill, name="show_skill"),
    path("project/", show_project, name="show_project"),
    path("project/add/", create_project, name="create_project"),
    path("api/project/", get_project_json, name="get_project_json"),
    path("project/<uuid:project_id>/delete/",delete_project,name="delete_project")
]