from typing import Any

from django.views.generic import TemplateView
from lecturers.models import LecturerCourse
from programs.models import Program
from intakes.models import Intake

# Create your views here.


class AllocationView(TemplateView):
    template_name = "allocations/index.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["intake"] = Intake.objects.latest("created_at")
        context["programs"] = Program.objects.all()
        allocations = LecturerCourse.objects.all().filter(intake=context["intake"])

        # if program in allocations

        context["intakes"] = Intake.objects.all()

        context["BSE"] = context["programs"].filter(code="BSE").first()
        context["BIST"] = context["programs"].filter(code="BIST").first()
        context["BCSF"] = context["programs"].filter(code="BCSF").first()
        context["BCS"] = context["programs"].filter(code="BCS").first()
        context["DCOMP"] = context["programs"].filter(code="DComp").first()
        context["BCE"] = context["programs"].filter(code="BCE").first()
        context["allocations"] = allocations

        return context
