from django import forms
from .models import Intake

class DateInput(forms.DateField):
    input_type = 'date'
    is_hidden = False

class IntakeCreateUpdateForm(forms.ModelForm):

    class Meta:
        model = Intake
        fields = ['name','start_date','end_date','academic_year','term','is_active']
        widgets ={
            'start_date': forms.widgets.DateTimeInput(
                attrs={'type':'datetime-local'}
            ),
            'end_date':forms.widgets.DateInput(
                attrs={'type':'date'}
            )
        }
        