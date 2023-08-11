from typing import Any, Dict, Mapping, Optional, Type, Union

from courses.models import Course
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from .models import Program


class ProgramCreateForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = [
            "name",
            "code",
            "years_of_study",
            "degree_level",
            "department",
            "details",
        ]


class ProgramCourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ["courses"]

    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
