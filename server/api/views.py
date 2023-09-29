from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import AllocationSerializer
from allocations.models import Allocation
from lecturers.models import LecturerCourse
# Create your views here.



class AllocationListView(ListAPIView):
    serializer_class = AllocationSerializer
    queryset = LecturerCourse.objects.all()
