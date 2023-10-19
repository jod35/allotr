"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("select2/", include("django_select2.urls")),
    path("auth/", include("users.urls"), name="auth"),
    path("", include("home.urls"), name="home"),
    path("i18n/", include("django.conf.urls.i18n")),
    path("courses/", include("courses.urls")),
    path("programs/", include("programs.urls")),
    path("departments/", include("departments.urls")),
    path("schools/", include("schools.urls")),
    path("intakes/", include("intakes.urls")),
    path("enrollments/", include("enrollments.urls")),
    path("allocations/", include("allocations.urls")),
    path("lecturers/", include("lecturers.urls")),
    path("api/", include("api.urls")),
]
