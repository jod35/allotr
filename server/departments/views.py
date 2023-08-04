from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Department

# Create your views here.

class DepartmentListView(LoginRequiredMixin,ListView):
    template_name = 'departments/index.html'
    queryset = Department.objects.all()
