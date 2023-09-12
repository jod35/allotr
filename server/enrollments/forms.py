from django import forms
from programs.models import Enrollment


class EnrollmentCreateForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['intake','program','students_enrolled']