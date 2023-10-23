from django import forms
from lecturers.models import Lecturer

class LecturerCreateForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = '__all__'