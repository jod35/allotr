from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255,unique=True)
    code = models.CharField(max_length=5,unique=True)
    dean = models.CharField(max_length=250)
    contact_email = models.EmailField(max_length=80)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"