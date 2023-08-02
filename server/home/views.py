# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from courses.models import Course
from programs.models import Program
from departments.models import Department
from schools.models import School
from django.core.paginator import Paginator



@login_required(login_url="/auth/login/")
def index(request):

    course_count = Course.objects.count()
    program_count =Program.objects.count()
    department_count = Department.objects.count()
    school_count = School.objects.count()
    programs = Program.objects.all()

    
    departments = Department.objects.all()

    print(departments)

    context = {
        'course_count':course_count,
        'school_count':school_count,
        'department_count':department_count,
        'program_count':program_count,
        'departments':departments
    }

    return render(request,'home/index.html',context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
