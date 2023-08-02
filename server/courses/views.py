from django.shortcuts import render
from django.views.generic import ListView
from courses.models import Course
# Create your views here.

class CourseListView(ListView):
    template_name = 'courses/index.html'
    queryset  = Course.objects.all()


    
