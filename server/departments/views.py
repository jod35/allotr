from django.shortcuts import render
from django.views.generic import ListView
from .models import Department

# Create your views here.

class DepartmentListView(ListView):
    template_name = 'departments/index.html'
    queryset = Department.objects.all()
