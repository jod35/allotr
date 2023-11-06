from django.db import models
from programs.models import Enrollment
from lecturers.models import Lecturer

# Create your models here.
class Allocation(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    enrollments = models.ManyToManyField(Enrollment,related_name='enrollment')

    def __str__(self) -> str:
        return f"{self.lecturer.first_name} {self.lecturer.last_name}" 