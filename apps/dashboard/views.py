from itertools import chain

from django.shortcuts import render

from django.views.generic import TemplateView, CreateView,View
# Create your views here.
from apps.class_routine.models import Routine
from apps.course_material.models import CourseMaterial
from apps.node_activity.models import ActiveNode
from apps.notice.models import Notice
from apps.school.models import School
from apps.teacher.models import Teacher


class Dashboard(View):
    def get(self,request,*args,**kwargs):

        context={
            "active_node":ActiveNode.objects.all()
        }
        return render(request,'dashboard.html',context=context)


