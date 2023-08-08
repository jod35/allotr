from django.contrib import admin

from .models import Department


# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "school", "created_at"]
    search_fields = ["name"]
    list_filter = ["created_at"]
