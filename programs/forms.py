from typing import Any, Dict, Mapping, Optional, Type, Union

from courses.models import Course
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django_select2 import forms as s2forms

from .models import Program


class ProgramCourseWidget(s2forms.ModelSelect2MultipleWidget):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.attrs = {"style": "width: 100%"}

    search_fields = ["title__icontains", "code__icontains"]


class ProgramCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["details"].widget.attrs["rows"] = 5

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

        widgets = {"courses": ProgramCourseWidget}
