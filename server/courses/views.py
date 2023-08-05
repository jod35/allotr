from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView
from courses.models import Course
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseUpdateForm
# Create your views here.

# @login_required(login_url='/auth/login/')
class CourseListView(LoginRequiredMixin,ListView):
    template_name = 'courses/index.html'
    queryset  = Course.objects.all()
    context_object_name = 'courses'
    paginate_by = 10


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['update_form'] = CourseUpdateForm

        return context
    
