from django.db import models
from schools.models import School

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=500)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    department_head = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=80)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
