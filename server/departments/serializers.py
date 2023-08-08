from .models import Department
from rest_framework import serializers


class DepartmentCreateSerializer(serializers.ModelSerializer):
    model = Department
    fields = ["name", "department_head", "contact_email"]
