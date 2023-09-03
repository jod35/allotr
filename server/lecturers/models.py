from django.db import models
from courses.models import Course
from departments.models import Department
from intakes.models import Intake
from programs.models import Program

# Create your models here.
class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='lecturer_profiles/',default="lecturer.png", blank=True, null=True)
    join_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class LecturerCourse(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    program = models.ManyToManyField(Program, related_name='lecturer')
    intake =models.ForeignKey(Intake, on_delete=models.CASCADE,related_name='allocations')

    class Meta:
        unique_together = ('lecturer',)

    def __str__(self):
        return f"{self.lecturer} - {self.intake})"