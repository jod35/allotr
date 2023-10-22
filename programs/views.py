import json
from typing import Any, Dict

from courses.models import Course
from departments.models import Department
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView

from .forms import ProgramCourseUpdateForm, ProgramCreateForm
from .models import Program
from schools.models import School

# Create your views here.


class ProgramListView(ListView):
    template_name = "programs/index.html"
    queryset = Program.objects.all()
    context_object_name = "programs"
    paginate_by = 6
    form_class = ProgramCreateForm

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        context["form"] = ProgramCreateForm()

        return context
    


@login_required
def create_program(request: HttpRequest):
    data = json.loads(request.body)
    school  = School.objects.get(pk=1)

    new_program = Program(
        name=data.get("name"),
        code=data.get("code"),
        years_of_study=data.get("years_of_study"),
        details=data.get("details"),
        degree_level=data.get("degree_level"),
        department=Department.objects.get(id=data.get("department_id")),
        school =school
    )

    new_program.save()

    messages.success(request, "Program created successfully")
    return JsonResponse({"message": "Program created successfuly"})


class ProgramDetailView(LoginRequiredMixin, DetailView):
    model = Program
    template_name = "programs/details.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        program = self.get_object()

        context["form"] = ProgramCourseUpdateForm(instance=program)

        courses = self.get_object().courses.all()

        paginator = Paginator(courses, per_page=10)

        page_number = self.request.GET.get("page", 1)

        context["page_obj"] = paginator.page(page_number)

        return context

    def post(self, request, *args, **kwargs):
        program = self.get_object()

        form = ProgramCourseUpdateForm(data=request.POST, instance=program)

        if form.is_valid():
            # program instance has to be saved first
            program = form.save(commit=False)

            program.save()

            courses = form.cleaned_data.get("courses")

            program.courses.clear()
            for course in courses:
                program.courses.add(course)

            messages.success(request, "Courses updated successfully!")

            return redirect(reverse("program_detail", kwargs={"pk": program.id}))


@login_required
def updated_program(request: HttpRequest, program_id):
    data = json.loads(request.body)

    program = Program.objects.filter(id=program_id).update(**data)

    messages.success(request, "Program updated successfully")

    return JsonResponse({"message": f"Program `{program}` updated successfully"})


@login_required
def delete_program(request: HttpRequest, program_id):
    program = get_object_or_404(Program, id=program_id)

    program.delete()

    messages.success(request, "Program updated successfully")

    return JsonResponse({"message": "School deleted"})
