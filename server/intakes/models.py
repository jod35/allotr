from django.db import models
from datetime import datetime
from courses.models import Course

# Create your models here.

current_year = datetime.now().year


class Intake(models.Model):
    class Term(models.TextChoices):
        jan = "Jan", "January"
        may = "May", "May"
        sep = "Sep", "September"

    name = models.CharField(max_length=50)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateField(null=True)
    academic_year = models.IntegerField(default=current_year)
    term = models.CharField(max_length=25, choices=Term.choices, default=Term.jan)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    courses = models.ManyToManyField(Course, through="IntakeCourse")

    def __str__(self):
        return f"{self.term} {self.academic_year}"


class IntakeCourse(models.Model):
    intake = models.ForeignKey(Intake, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.intake.name} - {self.course.title}"
