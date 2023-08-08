from typing import Any, Dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from .forms import SchoolCreateForm
from django.http import HttpRequest, JsonResponse
from django.contrib import messages
import json

from .models import School

# Create your views here.


class SchoolListView(LoginRequiredMixin, ListView):
    template_name = "schools/index.html"
    queryset = School.objects.all()
    context_object_name = "schools"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        context['form'] = SchoolCreateForm()

        return context
    


class SchoolDetailView(LoginRequiredMixin, DetailView):
    template_name = "schools/details.html"
    context_object_name = "schools"
    queryset = School.objects.all()


def create_school(request:HttpRequest):

    data = json.loads(request.body)

    new_school =  School(**data)

    new_school.save()

    messages.success(request,"School created successfully")
    return JsonResponse({"message":"School created successfuly"})


def updated_school(request:HttpRequest):
    data = json.loads(request.body)

    return JsonResponse({"message":"School updated successfully"})
