from django import forms
from lecturers.models import Lecturer

class LecturerCreateForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['first_name','last_name','email','department','profile_picture']