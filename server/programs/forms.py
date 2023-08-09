from django import forms
from .models import Program


class ProgramCreateForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name','code','years_of_study','degree_level','department','details']