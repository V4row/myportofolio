from django.forms import ModelForm, TextInput, Textarea, URLInput
from django import forms
from django.conf import settings

from main.models import Project

class ProjectForm(ModelForm):
    secret_code = forms.CharField(
            label="Kode Rahasia",
            widget=forms.PasswordInput(
                attrs={"placeholder": "Masukkan kode rahasia"}
            ),
            required=True
        )

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
    def clean_secret_code(self):
        secret_code = self.cleaned_data.get("secret_code")
        expected_key = getattr(settings, "EDIT_KEY", "")

        if not expected_key or secret_code != expected_key:
            raise forms.ValidationError("Kode rahasia salah! Kamu tidak berhak menambah proyek.")
        return secret_code