from courses.models import Course
from departments.models import Department
from intakes.models import Intake
from lecturers.models import LecturerCourse, Lecturer
from programs.models import Enrollment, Program, ProgramStructure
from rest_framework import serializers


class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturerCourse
        fields = ["lecturer"]

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
        fields = ["id", "code", "title", "created_at", "course_description"]


class IntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intake
        fields = "__all__"


class IntakeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intake
        fields = ["id", "name", "academic_year", "term", "created_at", "is_active"]


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"


class DepartmentProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ["id", "code", "name", "degree_level"]


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class ProgramListSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Program
        fields = [
            "id",
            "name",
            "code",
            "degree_level",
            "details",
            "years_of_study",
            "department",
        ]


class EnrollmentListSerializer(serializers.ModelSerializer):
    program = ProgramSerializer()
    intake = IntakeSerializer()

    class Meta:
        model = Enrollment
        fields = ["id", "program", "intake", "students_enrolled"]

    def get_program(self, obj):
        # Serialize the program field, excluding the course field
        program_serializer = ProgramSerializer(obj.program)
        program_data = program_serializer.data
        program_data.pop("courses", None)  # Exclude the 'course' field
        return program_data

    def to_representation(self, instance):
        # Override to include the modified program representation
        representation = super().to_representation(instance)
        representation["program"] = self.get_program(instance)
        return representation


class EnrollmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ["students_enrolled"]


class ProgramCourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "code", "title", "course_description", "created_at"]


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturerCourse
        fields = ("lecturer",)


class CoursesInProgramSerializer(serializers.ModelSerializer):
    lecturer = LecturerSerializer(source="lecturer_set", many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "code", "title", "course_description", "created_at", "lecturer"]


class LecturerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ["id", "first_name", "last_name", "email"]


class LecturerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ["first_name", "last_name", "email"]


class ProgramStructureSerializer(serializers.ModelSerializer):
    program = ProgramSerializer()
    enrollment = EnrollmentListSerializer()
    courses = CourseListSerializer(many=True)

    class Meta:
        model = ProgramStructure
        fields = ["name", "program", "enrollment", "courses"]


class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramStructure
        fields = ["program", "enrollment", "courses", "name"]
