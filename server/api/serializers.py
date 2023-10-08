from allocations.models import Allocation
from courses.models import Course
from departments.models import Department
from intakes.models import Intake
from lecturers.models import LecturerCourse
from programs.models import Enrollment, Program
from rest_framework import serializers


class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturerCourse
        fields = ["lecturer", "courses"]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data[
            "lecturer"
        ] = f"{instance.lecturer.first_name} {instance.lecturer.last_name}"

        courses = instance.courses.all()

        course_names = [course.title for course in courses]

        # Assign courses directly to the data
        data["courses"] = course_names

        return data


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id","code", "title", "created_at","course_description"]


class IntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intake
        fields = "__all__"


class IntakeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intake
        fields = ["id","name", "academic_year","term", "created_at","is_active"]


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class ProgramListSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Program
        fields = ["id","name", "code", "degree_level", "department", "created_at","years_of_study","details"]


class EnrollmentListSerializer(serializers.ModelSerializer):
    program = ProgramSerializer()
    intake = IntakeSerializer()

    class Meta:
        model = Enrollment
        fields = ["id","program", "intake", "students_enrolled"]

class EnrollmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['students_enrolled']