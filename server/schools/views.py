from django.shortcuts import render
from django.views.generic import ListView
from .models import School
# Create your views here.


class SchoolListView(ListView):
    template_name = 'schools/index.html'
    queryset = School.objects.all()

