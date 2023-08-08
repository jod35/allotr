from django.contrib import admin
from .models import School

# Register your models here.


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ["name", "dean", "contact_email"]
    search_fields = ["name"]
    list_filter = ["created_at"]
