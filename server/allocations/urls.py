from django.urls import path
from . import views


urlpatterns = [
    path("", views.AllocationView.as_view(), name="allocation_list"),
]
