from django.urls import path

from . import views

urlpatterns = [
    path("allocations", views.AllocationListView.as_view(), name="allocation-list"),
    path("courses/", views.CourseListView.as_view(), name="course_api_list"),
    path("intakes/", views.IntakeListView.as_view(), name="intake_api_list"),
    path(
        "enrollments/", views.EnrollmentListView.as_view(), name="enrollment_api_list"
    ),
    path('programs/', views.ProgramListView.as_view(), name='program_api_list'),
    path('enrollment/<int:pk>/',views.EnrollmentDetailUpdateView.as_view(),name='enrollment_api_list'),
]
