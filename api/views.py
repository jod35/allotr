from allocations.models import Allocation
from courses.models import Course
from django.shortcuts import render
from intakes.models import Intake
from lecturers.models import LecturerCourse
from programs.models import Enrollment, Program
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    AllocationSerializer,
    CourseListSerializer,
    EnrollmentListSerializer,
    IntakeListSerializer,
    ProgramListSerializer,
    EnrollmentUpdateSerializer,
    ProgramCourseListSerializer,
    CoursesInProgramSerializer
)

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


class EnrollmentDetailUpdateView(GenericAPIView):
    serializer_class = EnrollmentUpdateSerializer
    queryset = Enrollment.objects.all()

    def post(self, request, pk):
        data = request.data

        enrollment = Enrollment.objects.get(pk=pk)

        serializer = self.serializer_class(instance=self.get_object(), data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProgramCourseListView(GenericAPIView):
    serializer_class = ProgramCourseListSerializer
    queryset = Program.objects.all()

    def get(self,request):
        programs = Course.objects.all()

        serializer = self.serializer_class(instance=programs,many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class CoursesInProgramListView(GenericAPIView):

    serializer_class = CoursesInProgramSerializer
    queryset = Course.objects.all()

    def get(self,request,program_id):
        program = Program.objects.get(id=program_id)

        courses_in_program = program.courses.all()

        result = self.serializer_class(
            instance=courses_in_program,
            many = True
        )

        return Response(data=result.data,status=status.HTTP_200_OK)        
 