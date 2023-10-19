from typing import Any, Dict

from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from lecturers.models import LecturerCourse
from programs.models import Program
from departments.models import Department
from .models import Allocation
from intakes.models import Intake

# Create your views here.


class AllocationView(TemplateView):
    template_name = "allocations/index.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["allocations"] = LecturerCourse.objects.all()
        context["programs"] = Program.objects.all()

        context["BSE"] = context['programs'].filter(code='BSE').first()
        context["BIST"] = context['programs'].filter(code='BIST').first()
        context["BCSF"] = context['programs'].filter(code='BCSF').first()
        context["BCS"] = context['programs'].filter(code='BCS').first()
        context["DCOMP"] = context['programs'].filter(code='DComp').first()
        context["BCE"] = context['programs'].filter(code='BCE').first()
        
        context["intake"] = Intake.objects.latest('created_at')
        return context
