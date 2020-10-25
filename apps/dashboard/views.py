from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
# Create your views here.




class Dashboard(TemplateView):
    template_name = 'dashboard.html'



