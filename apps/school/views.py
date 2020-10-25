from django.contrib.messages.views import SuccessMessageMixin
from django.forms import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, FormView

from apps.school.forms import SchoolCreateForm
from apps.school.models import School


def school(requests):
    return render(requests,'school_list.html')




class SchoolCreateAndListView(CreateView,SuccessMessageMixin):
    model = School
    form_class = SchoolCreateForm
    success_url = reverse_lazy('school:school')
    success_message = "School has been created Successfully"
    template_name = 'school_list.html'

    def get_context_data(self, **kwargs):
        context=super(SchoolCreateAndListView, self).get_context_data(*kwargs)
        context['object_list']= School.objects.all()
        return context

class SchoolDetailAndUpdateView(UpdateView):
    model = School
    form_class = SchoolCreateForm
    template_name = 'school_detail.html'

# redirect same page after update
    def get_success_url(self):
        self.success_url = HttpResponseRedirect("")

#getting current object data
    def get_context_data(self, **kwargs):
        context = super(SchoolDetailAndUpdateView, self).get_context_data(**kwargs)
        object = self.get_object()
        context['object'] = object
        return context
