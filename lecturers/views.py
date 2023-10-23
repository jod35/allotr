from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from .models import Lecturer
from .forms import LecturerCreateForm

# Create your views here.


class LecturerListView(ListView):
    template_name = "lecturers/index.html"
    queryset = Lecturer.objects.all()
    form_class = LecturerCreateForm

    def get_context_data(self, **kwargs: Any):
        
        context = super().get_context_data(**kwargs)

        context['form'] = self.form_class()

        return context