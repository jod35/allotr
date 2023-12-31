from django import forms
from django_select2 import forms as s2forms

from .models import Program, ProgramStructure


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
            "school",
        ]


class ProgramCourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ["courses"]

        widgets = {"courses": ProgramCourseWidget}


class EnrollmentWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "intake__name__icontains",
        "intake__academic_year__icontains",
    ]


class CourseWidget(s2forms.ModelSelect2MultipleWidget):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.attrs = {"style": "width: 100%"}

    search_fields = ["title__icontains", "code__icontains"]


class ProgramStructureForm(forms.ModelForm):
    class Meta:
        model = ProgramStructure
        fields = ["name", "courses", "enrollment"]
        widgets = {"courses": CourseWidget, "enrollments": EnrollmentWidget}
