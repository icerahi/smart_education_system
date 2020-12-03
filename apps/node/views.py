from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.node.forms import NodeForm
from apps.node.models import Node

class NodeListAndCreateView(SuccessMessageMixin,CreateView):
    model= Node
    form_class = NodeForm
    success_url = reverse_lazy('node:node')
    success_message = 'New Node has been created !'
    template_name = 'node_list.html'

    def get_context_data(self, **kwargs):
        context = super(NodeListAndCreateView, self).get_context_data(*kwargs)
        context['object_list'] = Node.objects.all()
        return context


class NodeDetailAndUpdateView(SuccessMessageMixin,UpdateView):
    model = Node
    form_class = NodeForm
    template_name = 'node_detail.html'
    success_message = 'Node has been updated !'

    def get_success_url(self):
        return self.request.POST['previous']

    def get_context_data(self, **kwargs):
        context = super(NodeDetailAndUpdateView, self).get_context_data(**kwargs)
        object = self.get_object()
        context['object']=object
        return context

def enable_disable(request,pk,slug):
    node = Node.objects.get(pk=pk,slug=slug)
    if node.status == 'disable':
        node.status='enable'
        node.save()
        return redirect('node:node')
    if node.status == 'enable':
        node.status ='disable'
        node.save()
        return redirect('node:node')

