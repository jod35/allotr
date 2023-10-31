from django.urls import path

from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
    openapi.Info(
        title="Allotr API",
        default_version="v1",
        description="A REST API for the Allotr Course Allocation system",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ssali.jkigundu@student.utamu.ac.ug"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("allocations", views.AllocationListView.as_view(), name="allocation-list"),
    path("courses/", views.CourseListView.as_view(), name="course_api_list"),
    path("intakes/", views.IntakeListView.as_view(), name="intake_api_list"),
    path(
        "enrollments/", views.EnrollmentListView.as_view(), name="enrollment_api_list"
    ),
    path("programs/", views.ProgramListView.as_view(), name="program_api_list"),
    path(
        "program/<int:program_id>/",
        views.ProgramDetailView.as_view(),
        name="program_detail",
    ),
    path(
        "programs-in-department/department/<int:department_id>/",
        views.ProgramsInDepartmentView.as_view(),
        name="programs_in_department_api_list",
    ),
    path(
        "enrollment/<int:pk>/",
        views.EnrollmentDetailUpdateView.as_view(),
        name="enrollment_api_list",
    ),
    path(
        "programcourses/",
        views.ProgramCourseListView.as_view(),
        name="program_course_api_list",
    ),
    path(
        "courses-in-program/<int:program_id>/",
        views.CoursesInProgramListView.as_view(),
        name="courses_in_program",
    ),
    path(
        "list_allocations/",
        views.ListAllocationView.as_view(),
        name="list_allocations_matching",
    ),
    path("lecturers/", views.LecturerList.as_view(), name="lecturer_api_list"),
    path(
        "lecturers/<int:lecturer_id>/",
        views.LecturerDetailView.as_view(),
        name="lecturer_api_detail",
    ),
]
