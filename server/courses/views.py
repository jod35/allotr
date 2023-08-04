from django.shortcuts import render
from django.views.generic import ListView
from courses.models import Course
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# @login_required(login_url='/auth/login/')
class CourseListView(LoginRequiredMixin,ListView):
    template_name = 'courses/index.html'
    queryset  = Course.objects.all()


    
