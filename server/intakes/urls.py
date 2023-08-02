from django.urls import path
from . import views

urlpatterns = [
    path('', views.IntakeListView.as_view(), name='intake_list'),
]