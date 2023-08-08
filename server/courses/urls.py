from django.urls import path
from . import views


urlpatterns = [
    path("", views.CourseListView.as_view(), name="course_list"),
    path("update/<int:course_id>", views.update_course, name="update_course"),
]
