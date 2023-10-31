from typing import Any

from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from programs.models import Enrollment

from .forms import EnrollmentCreateForm, EnrollmentUpdateForm

# Create your views here.


class EnrollmentListView(ListView):
    template_name = "enrollments/index.html"
    queryset = Enrollment.objects.all()

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["form"] = EnrollmentCreateForm()
        context["update_form"] = EnrollmentUpdateForm()
        context["enrollments"] = Enrollment.objects.all()
        return context

    def post(self, request: HttpRequest, *args, **kwargs):
        data = request.POST

        form = EnrollmentCreateForm(data=data)

        if form.is_valid():
            form.save()

        return redirect(reverse("enrollment_list"))
