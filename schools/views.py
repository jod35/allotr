import json
from typing import Any, Dict

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .forms import SchoolCreateForm
from .models import School

# Create your views here.


class SchoolListView(LoginRequiredMixin, ListView):
    template_name = "schools/index.html"
    queryset = School.objects.all()
    context_object_name = "schools"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        context["form"] = SchoolCreateForm()

        return context


class SchoolDetailView(LoginRequiredMixin, DetailView):
    template_name = "schools/details.html"
    context_object_name = "schools"
    queryset = School.objects.all()


@login_required
def create_school(request: HttpRequest):
    data = json.loads(request.body)

    new_school = School(**data)

    new_school.save()

    messages.success(request, "School created successfully")
    return JsonResponse({"message": "School created successfuly"})


@login_required
def updated_school(request: HttpRequest, school_id):
    data = json.loads(request.body)

    school = School.objects.filter(id=school_id).update(**data)

    messages.success(request, "School updated successfully")

    return JsonResponse({"message": f"School `{school}` updated successfully"})


@login_required
def delete_school(request: HttpRequest, school_id):
    school = get_object_or_404(School, id=school_id)

    school.delete()

    messages.success(request, "School updated successfully")

    return JsonResponse({"message": "School deleted"})
