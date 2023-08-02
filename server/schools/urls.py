from django.urls import path
from . import views
urlpatterns = [
    path('', views.SchoolListView.as_view(), name='school_list'),
]