from django import forms
from .models import RegistroMateria

class RegistroMateriaForm(forms.ModelForm):
    class Meta:
        model = RegistroMateria
        fields = ['nombre_materia', 'profesor', 'comentario', 'calificacion', 'semestre']
