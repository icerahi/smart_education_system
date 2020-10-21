from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from related_select.views import RelatedSelectView

from apps.school.models import District


class Dashboard(TemplateView):
    template_name = 'base.html'


#need to test
class MySelectView(RelatedSelectView):
    @staticmethod
    def filter(value,**kwargs):
        return District.objects.filter(division_id=value)

    @staticmethod
    def to_value(obj):
        return obj.uuid

    @staticmethod
    def to_text(obj):
        return '({}) {}'.format(obj.id,obj.name)

