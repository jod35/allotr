from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import AllocationSerializer,CourseListSerializer,IntakeListSerializer,EnrollmentListSerializer
from allocations.models import Allocation
from lecturers.models import LecturerCourse
from courses.models import Course
from intakes.models import Intake
from programs.models import Enrollment

# Create your views here.



class AllocationListView(ListAPIView):
    serializer_class = AllocationSerializer
    queryset = LecturerCourse.objects.all()

class CourseListView(ListAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()


class IntakeListView(ListAPIView):
    serializer_class = IntakeListSerializer
    queryset = Intake.objects.all()


class EnrollmentListView(ListAPIView):
    serializer_class = EnrollmentListSerializer
    queryset = Enrollment.objects.all()