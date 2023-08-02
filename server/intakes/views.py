from django.shortcuts import render
from django.views.generic import ListView
from .models import Intake
# Create your views here.

class IntakeListView(ListView):
    template_name = 'intakes/index.html'
    queryset = Intake.objects.all()
