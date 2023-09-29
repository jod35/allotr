from django.urls import path
from . import views

urlpatterns = [
    path('allocations',views.AllocationListView.as_view(),name='allocation-list'),
]