from typing import Any, Dict
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpRequest
from django.contrib import messages
from .forms import DepartmentUpdateForm
from .models import Department
import json

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


@login_required
def update_department(request:HttpRequest,department_id):
    department_to_update = Department.objects.filter(pk=department_id)

    print(request.is_ajax())

    if request.method == "POST" and request.is_ajax():
        data = json.loads(request.body)
        

        print(data)

        department_to_update.update(
                name = data.get('name'),
                description = data.get('description'),
                department_head = data.get('department_head'),
                contact_email = data.get('contact_email')
        )

        messages.success(request,f"Department '{department_to_update.first().name}' has been updated successfully")
       
        return JsonResponse(data={"message":"Updated Successfully"})

    return JsonResponse(data={"message":"Hello from server"})


