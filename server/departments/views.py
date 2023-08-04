from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DepartmentUpdateForm
from .models import Department

# Create your views here.

class DepartmentListView(LoginRequiredMixin,ListView):
    template_name = 'departments/index.html'
    queryset = Department.objects.all()
    context_object_name = 'departments'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context =  super().get_context_data(**kwargs)

        context['form'] = DepartmentUpdateForm()

        return context
 
class DepartmentDetailView(LoginRequiredMixin,DetailView):
    template_name = 'departments/detail.html'
    queryset = Department.objects.all()

