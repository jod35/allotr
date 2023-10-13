import json
from typing import Any, Dict

from django.contrib import messages
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .forms import IntakeCreateUpdateForm
from .models import Intake

# Create your views here.


class IntakeListView(ListView):
    template_name = "intakes/index.html"
    queryset = Intake.objects.all()
    context_object_name = "intakes"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        context["form"] = IntakeCreateUpdateForm()

        return context

    def post(self, request, *args, **kwargs):
        form = IntakeCreateUpdateForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Intake Createx successfully")
            return redirect(reverse("intake_list"))


class IntakeUpdateView(View):
    def post(self, request: HttpRequest, intake_id):
        data = json.loads(request.body)

        print(data)

        # query the intake to update
        intake = Intake.objects.get(id=intake_id)

        intake.name = data.get("name")
        intake.academic_year = data.get("academic_year")
        intake.start_date = data.get("start_date")
        intake.end_date = data.get("end_date")
        intake.term = data.get("term")
        intake.is_active = data.get("is_active")

        intake.save()

        messages.success(request, f"Intake {data.get('name')} updated successfully")
        return JsonResponse({"message": "yomama", "intake": data})
