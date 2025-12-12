from django import forms
from .models import Apunte, MaterialEstudio, Debate, MensajeDebate


class ApunteForm(forms.ModelForm):
    class Meta:
        model = Apunte
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }


class MaterialEstudioForm(forms.ModelForm):
    class Meta:
        model = MaterialEstudio
        fields = ['titulo', 'descripcion', 'archivo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }


class DebateForm(forms.ModelForm):
    class Meta:
        model = Debate
        fields = ['titulo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MensajeDebateForm(forms.ModelForm):
    class Meta:
        model = MensajeDebate
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
