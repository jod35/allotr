from courses.models import Course
from intakes.models import Intake
from lecturers.models import LecturerCourse, Lecturer
from programs.models import Enrollment, Program, ProgramStructure
from departments.models import Department
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.views import APIView
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
    CoursesInProgramSerializer,
    DepartmentProgramSerializer,
    LecturerListSerializer,
    LecturerDetailSerializer,
    ProgramStructureSerializer,
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

    def post(self, request):
        """Create enrollment"""
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProgramListView(ListAPIView):
    serializer_class = ProgramListSerializer
    queryset = Program.objects.all()

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProgramDetailView(GenericAPIView):
    serializer_class = ProgramListSerializer

    def get(self, request, program_id):
        """
        get a program

        Args:

            program_id (int): id of program
        """
        program = Program.objects.get(id=program_id)

        serializer = self.serializer_class(instance=program)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, program_id):
        """
        Update program information

        Args:
            program_id : id of program
        """
        program_to_update = Program.objects.get(id=program_id)

        data = request.data

        serializer = self.serializer_class(instance=program_to_update, data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, program_id):
        """
        delete a program

        Args:
            program_id : id of program
        """
        program_to_delete = Program.objects.get(id=program_id)

        program_to_delete.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ProgramsInDepartmentView(GenericAPIView):
    serializer_class = DepartmentProgramSerializer

    def get(self, request, department_id):
        department = Department.objects.filter(pk=department_id).first()
        programs = Program.objects.filter(department=department).all()
        serializer = self.serializer_class(instance=programs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EnrollmentDetailUpdateView(GenericAPIView):
    serializer_class = EnrollmentUpdateSerializer
    queryset = Enrollment.objects.all()

    def post(self, request, pk):
        """update enrollment

        Args:
            pk (int): pk for enrollment
        """
        data = request.data

        serializer = self.serializer_class(instance=self.get_object(), data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        Get all enrollments
        """
        enrollments = Enrollment.objects.all()
        result = self.serializer_class(instance=enrollments)

        return Response(data=result.data, status=status.HTTP_200_OK)


class ProgramCourseListView(GenericAPIView):
    serializer_class = ProgramCourseListSerializer
    queryset = Program.objects.all()

    def get(self, request):
        programs = Course.objects.all()

        serializer = self.serializer_class(instance=programs, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CoursesInProgramListView(GenericAPIView):
    serializer_class = CoursesInProgramSerializer
    queryset = Course.objects.all()

    def get(self, request, program_id):
        program = Program.objects.filter(id=program_id).first()
        structures = ProgramStructure.objects.filter(program=program).all()
        print(structures)

        result = ProgramStructureSerializer(instance=structures, many=True).data

        return Response(data=result, status=status.HTTP_200_OK)


class ListAllocationView(APIView):
    def get(self, request):
        intake = Intake.objects.latest("created_at")
        allocations = LecturerCourse.objects.all().filter(intake=intake).all()
        enrollments = Enrollment.objects.all().filter(intake=intake).all()
        course_list = Course.objects.all()
        programs = Program.objects.all()
        allocations = LecturerCourse.objects.filter()
        enrollments = Enrollment.objects.all()
        allocation_for_courses = []
        for course in course_list:
            for allocation in allocations:
                if course in allocation.courses.all():
                    alloc = {
                        "course": {"title": course.title, "code": course.code},
                        "lecturer": f"{allocation.lecturer.first_name} {allocation.lecturer.last_name}",
                        "matching": [
                            program.code
                            for program in programs
                            if (course in program.courses.all())
                        ],
                        "intake": allocation.intake.name,
                        "students": sum(
                            [
                                enrollment.students_enrolled
                                for enrollment in enrollments
                                if (course in enrollment.program.courses.all())
                            ]
                        ),
                    }

                    allocation_for_courses.append(alloc)

        return Response(data=allocation_for_courses, status=status.HTTP_200_OK)


class LecturerList(ListAPIView):
    serializer_class = LecturerListSerializer

    def get(self, request, *args, **kwargs):
        lecturers = Lecturer.objects.all()

        serializer = self.serializer_class(instance=lecturers, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class LecturerDetailView(GenericAPIView):
    serializer_class = LecturerDetailSerializer

    def put(self, request, lecturer_id):
        lecturer_to_update = Lecturer.objects.get(id=lecturer_id)
        serializer = self.serializer_class(
            instance=lecturer_to_update, data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
