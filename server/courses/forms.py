from django import forms
from .models import Course



class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code','title','course_description']