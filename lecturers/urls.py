from django.urls import path
from . import views

urlpatterns = [
    path("", views.LecturerListView.as_view(), name="lecturer_list"),
]
