from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView

from .models import School

# Create your views here.


class SchoolListView(LoginRequiredMixin, ListView):
    template_name = "schools/index.html"
    queryset = School.objects.all()
    context_object_name = "schools"


class SchoolDetailView(LoginRequiredMixin, DetailView):
    template_name = "schools/details.html"
    context_object_name = "schools"
    queryset = School.objects.all()
