from courses.models import Course
from departments.models import Department
from django.db import models
from intakes.models import Intake
from schools.models import School


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
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="department"
    )
    details = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    courses = models.ManyToManyField(Course, related_name="programs")
    semesters = models.ManyToManyField(Intake, through="Enrollment")
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("-created_at",)


class Enrollment(models.Model):
    program = models.ForeignKey(
        Program, on_delete=models.CASCADE, related_name="enrollments"
    )
    intake = models.ForeignKey(
        Intake, on_delete=models.CASCADE, related_name="enrollments"
    )
    students_enrolled = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"<{self.program} {self.intake.term} {self.intake.academic_year}"
