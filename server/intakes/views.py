from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView
from .forms import IntakeCreateUpdateForm

from .models import Intake

# Create your views here.


class IntakeListView(ListView):
    template_name = "intakes/index.html"
    queryset = Intake.objects.all()
    context_object_name = 'intakes'


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)


        context['form'] = IntakeCreateUpdateForm()
        

        return context