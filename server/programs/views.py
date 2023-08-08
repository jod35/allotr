from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from .models import Program

# Create your views here.


class ProgramListView(ListView):
    template_name = "programs/index.html"
    queryset = Program.objects.all()
