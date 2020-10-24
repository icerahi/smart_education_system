from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

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

