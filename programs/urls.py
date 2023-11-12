from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProgramListView.as_view(), name="program_list"),
    path("<int:pk>/", views.ProgramDetailView.as_view(), name="program_detail"),
    path("update/<int:program_id>/", views.updated_program, name="update_program"),
    path("delete/<int:program_id>/", views.delete_program, name="delete_program"),
    path(
        "structure/program/<int:program_id>/",
        views.ProgramCourseStructureView.as_view(),
        name="program_structure",
    ),
]
