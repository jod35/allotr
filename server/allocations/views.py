from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from .models import Allocation
# Create your views here.



class AllocationView(TemplateView):
    template_name ='allocations/index.html'
       



