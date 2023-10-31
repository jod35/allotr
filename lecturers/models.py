from courses.models import Course
from departments.models import Department
from django.db import models
from intakes.models import Intake


# Create your models here.
class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(
        upload_to="lecturer_profiles/", default="lecturer.png", blank=True, null=True
    )
    join_date = models.DateField(auto_now=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class LecturerCourse(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, related_name="lecturer")
    intake = models.ForeignKey(
        Intake, on_delete=models.CASCADE, related_name="allocations"
    )

    class Meta:
        unique_together = ("lecturer",)

    def __str__(self):
        return f"{self.lecturer} - {self.intake})"
