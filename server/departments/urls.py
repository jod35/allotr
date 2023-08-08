from django.urls import path
from . import views

urlpatterns = [
    path("", views.DepartmentListView.as_view(), name="department_list"),
    path("create/", views.create_department, name="create_department"),
    path("<int:pk>/", views.DepartmentDetailView.as_view(), name="department_detail"),
    path(
        "update/<int:department_id>/", views.update_department, name="department_update"
    ),
    path("delete/<int:pk>/", views.delete_department, name="delete_department"),
]
