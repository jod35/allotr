from rest_framework import serializers

from .models import Department


class DepartmentCreateSerializer(serializers.ModelSerializer):
    model = Department
    fields = ["name", "department_head", "contact_email"]
