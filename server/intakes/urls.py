from django.urls import path

from . import views

urlpatterns = [
    path("", views.IntakeListView.as_view(), name="intake_list"),
    path(
        "update/<int:intake_id>/",
        views.IntakeUpdateView.as_view(),
        name="update_intake",
    ),
]
