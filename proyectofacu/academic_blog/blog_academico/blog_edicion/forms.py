from django import forms
from .models import Articulo, Apunte


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ["titulo", "bajada", "cuerpo", "imagen"]

        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Título principal de la noticia",
                }
            ),
            "bajada": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Resumen corto o copete (aparece en la tarjeta)",
                }
            ),
            # Agrandé este campo a 10 líneas para que puedas escribir cómodo y poner links HTML
            "cuerpo": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 10,
                    "placeholder": "Escribe aquí la noticia completa. Puedes pegar enlaces HTML.",
                }
            ),
            "imagen": forms.FileInput(attrs={"class": "form-control"}),
        }

        # Etiquetas para que se vea más profesional en la pantalla
        labels = {
            "titulo": "Título",
            "bajada": "Bajada / Copete",
            "cuerpo": "Contenido de la Noticia",
            "imagen": "Imagen de Portada (Flyer)",
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
