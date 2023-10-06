from allocations.models import Allocation
from courses.models import Course
from django.shortcuts import render
from intakes.models import Intake
from lecturers.models import LecturerCourse
from programs.models import Enrollment, Program
from rest_framework.generics import ListAPIView

from .serializers import (AllocationSerializer, CourseListSerializer,
                          EnrollmentListSerializer, IntakeListSerializer,
                          ProgramListSerializer)

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

class ProgramListView(ListAPIView):
    serializer_class = ProgramListSerializer
    queryset = Program.objects.all()

