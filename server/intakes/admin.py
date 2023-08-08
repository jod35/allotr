from django.contrib import admin

from .models import Intake, IntakeCourse

# Register your models here.


@admin.register(Intake)
class IntakeAdmin(admin.ModelAdmin):
    list_display = ["name", "academic_year", "term", "created_at"]
    search_fields = ["academic_year", "term"]
    # date_hierarchy = ['start_date']


admin.site.register(IntakeCourse)
