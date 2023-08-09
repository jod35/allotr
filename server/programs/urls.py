from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProgramListView.as_view(), name="program_list"),
    path("create/",views.create_program,name='create_program'),
    path("update/<int:program_id>/",views.updated_program,name='update_program'),
    path("delete/<int:program_id>/",views.delete_program,name='delete_program'),
]

