from django.contrib import admin
from .models import Program

# Register your models here.


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "department", "years_of_study", "degree_level"]
    list_filter = ["created_at", "years_of_study"]
    search_fields = ["name"]
