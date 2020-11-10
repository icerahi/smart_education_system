from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from apps.teacher.forms import TeacherForm
from apps.teacher.models import Teacher


class IndexView(TemplateView):
    template_name = 'teacher_list.html'


class TeacherCreateAndListView(SuccessMessageMixin,CreateView):
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('teacher:teacher')
    success_message = 'New Teacher has been created!'
    template_name = 'teacher_list.html'

    def get_context_data(self, **kwargs):
        context=super(TeacherCreateAndListView, self).get_context_data(*kwargs)
        context['object_list'] = Teacher.objects.all()
        return context



class TeacherDetailAndUpdateView(SuccessMessageMixin,UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher_detail.html'
    success_message = "'%(name)s' has been updated!"

    def get_success_url(self):
        return self.request.POST['previous']

#passing details of a object with context
    def get_context_data(self, **kwargs):
        context = super(TeacherDetailAndUpdateView, self).get_context_data(**kwargs)
        object = self.get_object()
        context['object'] = object
        return context
