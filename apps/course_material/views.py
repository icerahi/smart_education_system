from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.course_material.forms import CourseMaterialForm
from apps.course_material.models import CourseMaterial, Class


class CourseMaterialCreateAndListView(SuccessMessageMixin,CreateView):
    model = CourseMaterial
    form_class = CourseMaterialForm
    template_name = 'course_material_list.html'
    success_url = reverse_lazy('course_material:course_material')
    success_message = "<strong>Material Created Successfully!</strong>"
    error_message = """<strong>Error creating New Course Material!</strong> \n Check the Create Form"""

    def form_valid(self, form):
        form = CourseMaterialForm(self.request.POST,self.request.FILES)
        return super(CourseMaterialCreateAndListView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,self.error_message )
        return super(CourseMaterialCreateAndListView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CourseMaterialCreateAndListView, self).get_context_data(**kwargs)
        context['classes'] = Class.objects.all()
        return context



class GetContentView(SuccessMessageMixin,CreateView):
    model = CourseMaterial
    form_class = CourseMaterialForm
    success_message = 'Content created successfully!'
    template_name = 'content_list.html'
    error_message = """<strong>Error creating New Course Material!</strong> \n Check the Create Form"""

    def get_success_url(self):
        return reverse_lazy('course_material:get_content',kwargs={'class_name':self.kwargs['class_name'],
                                                                  'subject':self.kwargs['subject']})

    def form_valid(self, form):
        form = CourseMaterialForm(self.request.POST,self.request.FILES)
        return super(GetContentView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,self.error_message )
        return super(GetContentView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(GetContentView, self).get_context_data(**kwargs)
        context['object_list']=CourseMaterial.objects.filter(class_name__name=self.kwargs['class_name'],subject__name=self.kwargs['subject'])
        context['classes']=Class.objects.all()
        context['subject']=self.kwargs['subject']
        context['class_name']=self.kwargs['class_name']
        return context



class ContentUpdateView(SuccessMessageMixin,UpdateView):
    model = CourseMaterial
    form_class = CourseMaterialForm
    success_message = 'Content has been updated!'
    template_name = 'content_update.html'

    def get_success_url(self):
        return reverse_lazy('course_material:get_content',kwargs={'class_name':self.kwargs['class_name'],
                                                                  'subject':self.kwargs['subject']})

    def get_context_data(self, **kwargs):
        context = super(ContentUpdateView, self).get_context_data(**kwargs)
        context['classes']=Class.objects.all()
        return context
