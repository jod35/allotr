from django.db import models
from courses.models import Course

# Create your models here.
class Program(models.Model):
    class DegreeLevel(models.TextChoices):
        diploma ="D","Diploma"
        bachelors = "B","Bachelors"
        postgrad = "PGd","PostGraduateDiploma"
        masters = "M", "Masters"


    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    years_of_study = models.IntegerField(default=3)
    degree_level = models.CharField(max_length=50,choices=DegreeLevel.choices)
    details = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    courses = models.ManyToManyField(Course,through="ProgramCourse")

    def __str__(self) -> str:
        return self.name
    

class ProgramCourse(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.program.program_name} - {self.course.course_title}"