from django import forms

from .models import Department


class DepartmentUpdateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))

    class Meta:
        model = Department
        fields = ["name", "department_head", "contact_email", "description"]


class DepartmentCreateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))

    class Meta:
        model = Department
        fields = ["name", "department_head", "school", "contact_email", "description"]
