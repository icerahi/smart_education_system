from django.forms import ModelForm

from apps.node.models import Node


class NodeForm(ModelForm):
    class Meta:
        model = Node
        fields = ('ip_address','port','mac_address','school_id','class_name','status')
        
    def __init__(self,*args,**kwargs):
        _school_set = kwargs.pop('school_set',None)
        super(NodeForm, self).__init__(*args,**kwargs)
        self.fields['ip_address'].widget.attrs['class'] = 'form-control'
        self.fields['port'].widget.attrs['class'] = 'form-control'
        self.fields['mac_address'].widget.attrs['class'] = 'form-control'
        self.fields['school_id'].widget.attrs['class'] = 'form-control'
        self.fields['class_name'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'


