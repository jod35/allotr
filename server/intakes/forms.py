from django import forms
from .models import Intake



class IntakeCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Intake
        fields = ['name','start_date','end_date','academic_year','term','is_active']