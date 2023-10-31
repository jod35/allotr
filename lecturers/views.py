from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from .models import Lecturer
from .forms import LecturerCreateForm
from django.contrib import messages

# Create your views here.


class LecturerListView(ListView):
    template_name = "lecturers/index.html"
    queryset = Lecturer.objects.all()
    form_class = LecturerCreateForm

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        context["form"] = self.form_class()

        return context

    def post(self, request):
        form = self.form_class(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, message="Lecturer added successfully")

            return redirect(reverse("lecturer_list"))

        return render(request, self.template_name)
