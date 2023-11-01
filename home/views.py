# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from courses.models import Course
from departments.models import Department
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from programs.models import Program
from schools.models import School
from django.db.models import Sum
from slick_reporting.views import ReportView, Chart
from slick_reporting.fields import ComputationField
from lecturers.models import Lecturer, LecturerCourse
from programs.models import Enrollment


@login_required(login_url="/auth/login/")
def index(request):
    course_count = Course.objects.count()
    program_count = Program.objects.count()
    department_count = Department.objects.count()
    school_count = School.objects.count()
    
    departments = Department.objects.all()

    context = {
        "course_count": course_count,
        "school_count": school_count,
        "department_count": department_count,
        "program_count": program_count,
        "departments": departments,
    }

    return render(request, "home/index.html", context)


@login_required(login_url="/auth/login")
def profile_page(request):
    return render(request, "home/profile.html")




class TotalStudentsAllocationView(ReportView):
    report_model = Program
    group_by = "courses"
    date_field ="created_at"
    columns = [
        "title",
        "code"
    ]

