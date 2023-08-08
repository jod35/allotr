from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import School
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

# Create your views here.


class SchoolListView(LoginRequiredMixin, ListView):
    template_name = "schools/index.html"
    queryset = School.objects.all()
    context_object_name = "schools"


class SchoolDetailView(LoginRequiredMixin, DetailView):
    template_name = "schools/details.html"
    context_object_name = "schools"
    queryset = School.objects.all()
