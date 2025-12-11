from django import forms
from .models import Articulo, Apunte


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ["titulo", "bajada", "cuerpo", "imagen"]
        widgets = {
            "titulo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Título de la noticia"}
            ),
            "bajada": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Resumen corto"}
            ),
            "cuerpo": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "imagen": forms.FileInput(attrs={"class": "form-control"}),
        }


class ApunteForm(forms.ModelForm):
    class Meta:
        model = Apunte
        fields = ["titulo", "materia", "tipo", "archivo"]
        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Resumen Primer Parcial",
                }
            ),
            "materia": forms.Select(attrs={"class": "form-select"}),
            "tipo": forms.Select(attrs={"class": "form-select"}),
            "archivo": forms.FileInput(attrs={"class": "form-control"}),
        }
