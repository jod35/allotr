import json
from typing import Any, Dict

from courses.models import Course
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .forms import CourseUpdateForm

# Create your views here.


# @login_required(login_url='/auth/login/')
class CourseListView(LoginRequiredMixin, ListView):
    template_name = "courses/index.html"
    queryset = Course.objects.all()
    context_object_name = "courses"
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["update_form"] = CourseUpdateForm

        return context


@login_required
def update_course(request: HttpRequest, course_id):
    course_to_update = Course.objects.filter(id=course_id)
    if request.method == "POST" and request.is_ajax():
        data = json.loads(request.body)

        course_to_update.update(
            code=data.get("code"),
            title=data.get("title"),
            course_description=data.get("course_description"),
        )

        messages.success(
            request, f"Course '{course_to_update}' has been updated successfully!"
        )

        return JsonResponse(data={"message": "Course Updated successfully"})

    return JsonResponse(data={"message": "Hello from server"})
