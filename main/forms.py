from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateTimeInput
from main.models import Project, Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "url",
            "thumbnail",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Touching Grass",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title" : "Nama Pengalaman",
            "description" : "Deskripsi Pengalaman",
            "category" : "Kategori Pengalaman",
            "thumbnail" : "Gambar Pengalaman",
            "started_at": "Waktu mulai Pengalaman",
            "ended_at": "Waktu berakhir Pengalaman",
        }
        
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Lomba Tidur",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Memenangkan lomba bisa tidur dimana saja",
                    "rows" : 3
                }
            ),
            "category": Select(
                attrs={
                "placeholder": "Pilih kategori pengalaman"
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000"
                }
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "placeholder": "Kapan pengalaman ini berakhir",
                    "type": "date",
                }
            ) 
        }