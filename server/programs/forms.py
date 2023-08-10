from django import forms
from .models import Program
from courses.models import Course


class ProgramCreateForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name','code','years_of_study','degree_level','department','details']


class ProgramCourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['courses']

    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )