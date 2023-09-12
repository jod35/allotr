from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from programs.models import Enrollment
from .forms import EnrollmentCreateForm
# Create your views here.


class EnrollmentListView(ListView):
    template_name = 'enrollments/index.html'
    queryset = Enrollment.objects.all()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['form'] = EnrollmentCreateForm()
        context['enrollments'] = Enrollment.objects.all()
        return context
