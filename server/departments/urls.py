from django.urls import path
from . import views

urlpatterns = [
    path('', views.DepartmentListView.as_view(), name='department_list'),
    path('<int:pk>/',views.DepartmentDetailView.as_view(),name='department_detail'),
    path('update/<int:department_id>/',views.update_department, name='department_update'),
]