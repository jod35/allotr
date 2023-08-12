from typing import Any, Dict
from django.shortcuts import render,redirect
from django.views.generic import ListView
from .forms import IntakeCreateUpdateForm
from django.urls import reverse
from django.contrib import messages

from .models import Intake

# Create your views here.


class IntakeListView(ListView):
    template_name = "intakes/index.html"
    queryset = Intake.objects.all()
    context_object_name = 'intakes'


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)


        context['form'] = IntakeCreateUpdateForm()
        

        return context

    def post(self,request,*args,**kwargs):
        form = IntakeCreateUpdateForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Intake Createx successfully")
            return redirect(reverse('intake_list'))