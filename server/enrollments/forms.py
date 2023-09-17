from django import forms
from django_select2 import forms as s2forms
from programs.models import Enrollment

class EnrollmentWidget(s2forms.ModelSelect2Widget):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.attrs = {"style": "width: 100%"}

    search_fields =[
        "intake__academic_year__icontains",
        "program__name__icontains"
    ]


class EnrollmentCreateForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['intake','program','students_enrolled']



class EnrollmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['intake', 'program', 'students_enrolled']
    
    def __init__(self, *args, **kwargs):
        super(EnrollmentUpdateForm, self).__init__(*args, **kwargs)
        # Mark intake and program fields as disabled
        self.fields['intake'].widget.attrs['disabled'] = True
        self.fields['program'].widget.attrs['disabled'] = True