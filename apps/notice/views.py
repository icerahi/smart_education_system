from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from apps.notice.forms import NoticeForm
from apps.notice.models import Notice


class NoticeListAndCreateView(SuccessMessageMixin,CreateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'notice_list.html'
    success_url = reverse_lazy('notice:notice')
    success_message = "<strong>Notice has been created Successfully!</strong>"
    error_message   = "<strong>Error Creating New Notice ! </strong> \n Check the Create Form"

    def form_invalid(self, form):
        messages.error(self.request,self.error_message)
        return super(NoticeListAndCreateView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(NoticeListAndCreateView, self).get_context_data(**kwargs)
        context['object_list'] = Notice.objects.all()
        return context

class NoticeDetailAndUpdateView(SuccessMessageMixin,UpdateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'notice_detail.html'
    success_message = "Notice has been updated!"

    def get_success_url(self):
        return self.request.POST['previous']


    def get_context_data(self, **kwargs):
        context = super(NoticeDetailAndUpdateView, self).get_context_data(**kwargs)
        object  = self.get_object()
        context['object'] = object
        return context

def notice_status(request,pk,status):
    notice = Notice.objects.get(pk=pk)
    if status == 'published':
        notice.status='published'
        notice.save()
        messages.success(request,'<strong>Notice has been published successfully!</strong>')
        return redirect('notice:notice_detail',pk=pk)
    if status == 'archived':
        notice.status = 'archived'
        notice.save()
        messages.success(request, '<strong>Notice has been move to archived successfully!</strong>')
        return redirect('notice:notice_detail',pk=pk)
