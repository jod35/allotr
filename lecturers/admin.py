from django.contrib import admin
from lecturers.models import Lecturer, LecturerCourse

# Register your models here.


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "profile_picture", "email"]
    list_filter = ["join_date"]
    search_fields = ["first_name", "last_name"]


@admin.register(LecturerCourse)
class LecturerCourseAdmin(admin.ModelAdmin):
    list_display = ["lecturer", "intake"]
