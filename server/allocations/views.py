from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Allocation
from lecturers.models import LecturerCourse

# Create your views here.


class AllocationView(TemplateView):
    template_name = "allocations/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)

        context['allocations'] = LecturerCourse.objects.all()

        return context