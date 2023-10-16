from django import forms

from .models import Course


class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["code", "title", "course_description"]


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["code", "title", "course_description"]

        widgets ={
            'course_description':forms.Textarea(attrs={'rows':5})
        }
