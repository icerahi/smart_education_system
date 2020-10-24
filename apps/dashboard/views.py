from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from related_select.views import RelatedSelectView

from apps.school.models import District, Division


class Dashboard(TemplateView):
    template_name = 'dashboard.html'



#need to test


def load_address(request):
    pass