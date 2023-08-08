from django.db import models
from courses.models import Course
from departments.models import Department


# Create your models here.
class Program(models.Model):
    class DegreeLevel(models.TextChoices):
        diploma = "D", "Diploma"
        bachelors = "B", "Bachelors"
        postgrad = "PGd", "PostGraduateDiploma"
        masters = "M", "Masters"

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    years_of_study = models.IntegerField(default=3)
    degree_level = models.CharField(max_length=50, choices=DegreeLevel.choices)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    details = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    courses = models.ManyToManyField(Course, related_name="programs")

    def __str__(self) -> str:
        return self.name
