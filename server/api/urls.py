from django.urls import path
from . import views

urlpatterns = [
    path('allocations',views.AllocationListView.as_view(),name='allocation-list'),
    path('courses/',views.CourseListView.as_view(),name='course_api_list')
]