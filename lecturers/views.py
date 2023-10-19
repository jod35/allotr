from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from .models import Lecturer
# Create your views here.


class LecturerListView(ListView):
    template_name = 'lecturers/index.html'
    queryset = Lecturer.objects.all()

    def get_context_data(self, **kwargs: Any):
        return super().get_context_data(**kwargs)
