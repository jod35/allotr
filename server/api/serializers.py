from rest_framework import serializers
from allocations.models import Allocation
from lecturers.models import LecturerCourse
from courses.models import Course
from intakes.models import Intake
from programs.models import Program,Enrollment

class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturerCourse
        fields = ['lecturer','courses']


    def to_representation(self, instance):
        data =  super().to_representation(instance)

        data['lecturer'] = f"{instance.lecturer.first_name} {instance.lecturer.last_name}"

        courses = instance.courses.all()

        course_names = [course.title for course in courses]


        # Assign courses directly to the data
        data['courses'] = course_names
        
        return data
    
class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['code','title','created_at']

class IntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intake
        fields = "__all__"

class IntakeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intake
        fields = ['name','academic_year','term','created_at']

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"

class EnrollmentListSerializer(serializers.ModelSerializer):
    program = ProgramSerializer()
    intake = IntakeSerializer()

    class Meta:
        model = Enrollment
        fields = ['program','intake','students_enrolled']     