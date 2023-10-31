# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path

from . import views

urlpatterns = [
    # The home page
    path("", views.index, name="home"),
    path("profile/", views.profile_page, name="profile"),
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
]
