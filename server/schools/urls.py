from django.urls import path

from . import views

urlpatterns = [
    path("", views.SchoolListView.as_view(), name="school_list"),
    path("<int:pk>/", views.SchoolDetailView.as_view(), name="school_detail"),
    path("create/",views.create_school,name='create_school'),
    path("update/<int:school_id>/",views.updated_school,name='update_school'),
    path("delete/<int:school_id>/",views.delete_school,name='delete_school'),
]
