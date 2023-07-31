from django.db import models
from departments.models import Department
# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=10 , unique = True)
    title = models.CharField(max_length=225 )
    course_description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.code} {self.title}"
    

