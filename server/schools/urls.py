from django.urls import path

from . import views

urlpatterns = [
    path("", views.SchoolListView.as_view(), name="school_list"),
    path("<int:pk>/", views.SchoolDetailView.as_view(), name="school_detail"),
]
