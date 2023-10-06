from django.urls import path
from . import views


urlpatterns = [
    path("", views.EnrollmentListView.as_view(), name="enrollment_list"),
]
