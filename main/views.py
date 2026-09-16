from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect, render
from django.conf import settings

from main.models import Experience, Skill, Project
from main.forms import ProjectForm


def is_authorized(request):
    expected_key = getattr(settings, "EDIT_KEY", "")
    if not expected_key:
        return False

    header_key = request.META.get("HTTP_X_SECRET_KEY")
    if header_key and header_key == expected_key:
        return True

    body_key = request.POST.get("secret_code")
    if body_key and body_key == expected_key:
        return True

    return False

def show_main(request):
    context = {
        "name": "Vebian Francois Ariftya Manurung",
        "npm": "2506543363",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS student at Universitas Indonesia, "
            "just trying something new and fun."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Vebian Francois Ariftya Manurung",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_skill(request):
    context = {
        "name" : "Vebian Francois Ariftya Manurung",
        "skill_list" : Skill.objects.all(), 
    }
    return render(request, "skill.html", context)

def show_project(request):
    json_response = get_project_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name" : "Vebian Francois Ariftya Manurung",
        "project_list" : projects, 
        "title_query" : title_query,
    }
    return render(request, "project.html", context)

def create_project(request):
    if request.method == "POST" and request.META.get("HTTP_X_SECRET_KEY") == getattr(settings, "EDIT_KEY", ""):
        form = ProjectForm(request.POST)
        if "secret_code" in form.fields:
            form.fields["secret_code"].required = False
    else:
        form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_project")

    context = {
        "name": "Vebian Francois Ariftya Manurung",
        "form": form,
    }
    return render(request, "project_form.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if not is_authorized(request):
            messages.error(request, "Kode rahasia salah! Proyek batal dihapus.")
            return redirect("main:show_project")
            
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_project")

    return redirect("main:show_project")

def get_project_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")