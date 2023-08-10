from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView,DetailView
from django.http import JsonResponse,HttpRequest
from django.http import HttpRequest
from .models import Program
from departments.models import Department
from .forms import ProgramCreateForm, ProgramCourseUpdateForm
import json

# Create your views here.


class ProgramListView(ListView):
    template_name = "programs/index.html"
    queryset = Program.objects.all()
    context_object_name = 'programs'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)

        context['form'] = ProgramCreateForm()

        return context

@login_required
def create_program(request:HttpRequest):

    data = json.loads(request.body)
    print(data)

    new_program =  Program(
        name = data.get('name'),
        code = data.get('code'),
        years_of_study = data.get('years_of_study'),
        details = data.get('details'),
        degree_level = data.get('degree_level'),
        department = Department.objects.get(id=data.get('department_id'))
    )

    new_program.save()

    messages.success(request,"Program created successfully")
    return JsonResponse({"message":"Program created successfuly"})



class ProgramDetailView(LoginRequiredMixin,DetailView):
    model = Program
    template_name = "programs/details.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        context['form'] = ProgramCourseUpdateForm()

        return context


@login_required
def updated_program(request:HttpRequest,program_id):
    data = json.loads(request.body)

    program = Program.objects.filter(id =program_id).update(**data)

    messages.success(request,"Program updated successfully")

    return JsonResponse({"message":f"Program `{program}` updated successfully"})

@login_required
def delete_program(request:HttpRequest,program_id):

    program = get_object_or_404(Program,id = program_id)

    program.delete()

    messages.success(request,"Program updated successfully")

    return JsonResponse({"message":"School deleted"})
