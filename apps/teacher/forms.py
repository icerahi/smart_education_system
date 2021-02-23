from django.forms import ModelForm

from apps.teacher.models import Teacher
from django import forms

#for showing free text in form
# from django import forms
# class ListTextWidget(forms.TextInput):
#     def __init__(self, data_list, name, *args, **kwargs):
#         super(ListTextWidget, self).__init__(*args, **kwargs)
#         self._name = name
#         self._list = data_list
#         self.attrs.update({'list': 'list__%s' % self._name})
#     def render(self, name, value, attrs=None, renderer=None):
#         text_html = super(ListTextWidget, self).render(
#             name, value, attrs=attrs)
#         data_list = '<datalist id="list__%s">' % self._name
#         for item in self._list:
#             data_list += '<option class="form-control" value="%s">' % item
#         data_list += '</datalist>'
#         return (text_html + data_list)

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('name','image','designation','school_id',)

    def __init__(self,*args,**kwargs):
        _school_set = kwargs.pop('school_set',None)
        super(TeacherForm, self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['designation'].widget.attrs['class'] = 'form-control'
        self.fields['school_id'].widget.attrs['class'] = 'form-control'
       # self.fields['school_id'].widget=ListTextWidget(data_list=_school_set,name='school_set')




