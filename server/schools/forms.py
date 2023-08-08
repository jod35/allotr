from django import forms
from .models import School



class SchoolCreateForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name','code','dean','contact_email','details']
