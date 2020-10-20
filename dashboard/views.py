from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



class Dashboard(TemplateView):
    template_name = 'base.html'

class SchoolListview(TemplateView):
    template_name = 'school_list.html'
