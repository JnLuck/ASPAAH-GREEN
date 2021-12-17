from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
        'pers_nombre', 'pers_ape_paterno', 
        'pers_ape_materno', 'pers_dni', 
        'pers_fecha_nac', 'pers_civil', 
        'pers_sexo', 'pers_telefono', 
        'pers_email', 'pers_direccion', 
        # 'pers_estado', 
        'pers_parent',
    ]