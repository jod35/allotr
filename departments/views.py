import json
from typing import Any, Dict

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from programs.models import Program

from .forms import DepartmentCreateForm, DepartmentUpdateForm
from .models import Department

# Create your views here.


class DepartmentListView(LoginRequiredMixin, ListView):
    template_name = "departments/index.html"
    queryset = Department.objects.all()
    context_object_name = "departments"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["form"] = DepartmentCreateForm()

        return context


class DepartmentDetailView(LoginRequiredMixin, DetailView):
    template_name = "departments/detail.html"
    queryset = Department.objects.all()
    context_object_name = "department"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        context["departments"] = Department.objects.all()
        context["programs"] = Program.objects.all().filter(department=self.get_object())
        return context


@login_required
def create_department(request):
    if request.method == "POST":
        data = request.POST
        form = DepartmentCreateForm(data=data)

        if form.is_valid():
            form.save()

            messages.success(request, "Department created successfully")

            return redirect(reverse("department_list"))

    return redirect(reverse("department_list"))


@login_required
def update_department(request: HttpRequest, department_id):
    department_to_update = Department.objects.filter(pk=department_id)

    print(request.is_ajax())

    if request.method == "POST" and request.is_ajax():
        data = json.loads(request.body)

        print(data)

        department_to_update.update(
            name=data.get("name"),
            description=data.get("description"),
            department_head=data.get("department_head"),
            contact_email=data.get("contact_email"),
        )

        messages.success(
            request,
            f"Department '{department_to_update.first().name}' has been updated successfully",
        )

        return JsonResponse(data={"message": "Updated Successfully"})

    return JsonResponse(data={"message": "Hello from server"})


@login_required
def delete_department(request, pk):
    department = get_object_or_404(Department, id=pk)

    department.delete()

    messages.success(request, f"Department {department.name} deleted successfully")

    return redirect(reverse("department_list"))
