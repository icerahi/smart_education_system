from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

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
        context['contents'] = CourseMaterial.objects.all()
        context['classes'] = Class.objects.all()
        return context


def get_content(request,class_name,subject):

    content = CourseMaterial.objects.filter(class_name__name=class_name,subject__name=subject)
    context ={
        'object_list':content,
        'classes':Class.objects.all(),
        'subject':subject,
        'class_name':class_name,
    }
    return render(request,'content_list.html',context)