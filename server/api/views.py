from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import AllocationSerializer,CourseListSerializer
from allocations.models import Allocation
from lecturers.models import LecturerCourse
from courses.models import Course
# Create your views here.



class AllocationListView(ListAPIView):
    serializer_class = AllocationSerializer
    queryset = LecturerCourse.objects.all()

class CourseListView(ListAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()



