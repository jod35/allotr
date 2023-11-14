import json
from typing import Any

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views import View

from .forms import ProgramCourseUpdateForm, ProgramStructureForm, ProgramCreateForm
from .models import Program, ProgramStructure

# Create your views here.


class ProgramListView(LoginRequiredMixin, View):
    template_name = "programs/index.html"
    queryset = Program.objects.all()
    context_object_name = "programs"
    paginate_by = 6
    form_class = ProgramCreateForm

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        context["form"] = ProgramCreateForm()

        return context

    def get(self, request: HttpRequest):
        try:
            return render(request, self.template_name, {"form": self.form_class()})

        except Exception as e:
            import traceback

            traceback.print_exc()
            return HttpResponse(content=str(e))

    def post(self, request: HttpRequest):
        try:
            form = self.form_class(data=request.POST)

            if form.is_valid():
                form.save()

                program = form.instance
                return redirect(
                    reverse("program_structure", kwargs={"program_id": program.id})
                )

            messages.error(request, message=form.errors)
            return render(request, self.template_name, {"form": self.form_class()})

        except Exception as e:
            raise Exception(e)


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


class ProgramCourseStructureView(View):
    template_name = "programs/structures.html"
    form_class = ProgramStructureForm

    def get(self, request, program_id):
        program = get_object_or_404(Program, id=program_id)

        form = ProgramStructureForm()

        for year in range(program.years_of_study):
            new_semester = ProgramStructure(program=program)

            new_semester.save()

        context = {"form": form, "program": program}

        return render(request, self.template_name, context)


[
    {
        "structure": {
            "name": "Year 1 sem 1",
            "enrollment": "Sep 2023",
            "courses": {
                "code": "CS 101",
                "title": "Computer Applications And Systems",
                "lecturer": "Kivumbi Timothy",
                "matching": "BIST,BSE,BCS,BCE",
                "students": 2,
            },
        }
    }
]
