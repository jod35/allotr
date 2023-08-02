from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import School
# Create your views here.


class SchoolListView(ListView):
    template_name = 'schools/index.html'
    queryset = School.objects.all()
    context_object_name = 'schools'
    
    
class SchoolDetailView(DetailView):
    template_name = 'schools/details.html'
    context_object_name = 'schools'
    queryset = School.objects.all()

