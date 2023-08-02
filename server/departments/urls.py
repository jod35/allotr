from django.urls import path
from . import views

urlpatterns = [
    path('', views.DepartmentListView.as_view(), name='department_list'),
]