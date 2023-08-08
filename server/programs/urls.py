from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProgramListView.as_view(), name="program_list"),
]
