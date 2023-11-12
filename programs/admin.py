from django.contrib import admin

from .models import Enrollment, Program, ProgramStructure

# Register your models here.


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "department", "years_of_study", "degree_level"]
    list_filter = ["created_at", "years_of_study"]
    search_fields = ["name"]
    # filter_horizontal = ['courses']


admin.site.register(Enrollment)


admin.site.register(ProgramStructure)
