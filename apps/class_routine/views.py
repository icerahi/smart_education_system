from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import IntegrityError
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.class_routine.forms import RoutineForm
from apps.class_routine.models import Routine
from apps.course_material.models import Class


class RoutineCreateAndListView(SuccessMessageMixin,CreateView):
    model = Routine
    form_class = RoutineForm
    template_name = 'routine_base.html'
    success_message = "<strong>Routine Created Successfully!</strong>"
    error_message   = "<strong>Error Creating new routine ! </strong> \n Check the create form</strong>"
    success_url = reverse_lazy('class_routine:routine')

    def form_invalid(self, form):
        messages.error(self.request,self.error_message)
        return super(RoutineCreateAndListView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(RoutineCreateAndListView, self).get_context_data(**kwargs)
        context['classes'] = Class.objects.all()
        return context

class GetRoutineView(SuccessMessageMixin,CreateView):
    model = Routine
    form_class = RoutineForm
    template_name = 'routine_list.html'
    success_message = "<strong>Routine Created Successfully!</strong>"
    error_message   = "<strong>Error Creating new routine ! </strong> \n Check the create form</strong>"

    def get_success_url(self):
        return reverse_lazy('class_routine:routine',kwargs={'class_name':self.kwargs['class_name']})
    
    def form_invalid(self, form):
        messages.error(self.request,self.error_message)
        return super(GetRoutineView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(GetRoutineView, self).get_context_data(**kwargs)
        context['classes'] = Class.objects.all()
        context['class_name'] = self.kwargs['class_name']
        context['object_list'] = Routine.objects.filter(class_name__name=self.kwargs['class_name'])
        return context