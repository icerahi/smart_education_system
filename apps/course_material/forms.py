from django.forms import ModelForm

from apps.course_material.models import CourseMaterial


class CourseMaterialForm(ModelForm):

    class Meta:
        model = CourseMaterial
        fields =('class_name','subject','unit','content','unit_name',)

    def __init__(self,*args,**kwargs):
        super(CourseMaterialForm, self).__init__(*args,**kwargs)
        self.fields['class_name'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['unit'].widget.attrs['class'] = 'form-control'
        self.fields['unit_name'].widget.attrs['class'] = 'form-control'
        self.fields['unit_name'].widget.attrs['rows'] = '1'
        self.fields['unit_name'].widget.attrs['cols'] = '100'
        self.fields['content'].widget.attrs['class'] = 'form-control'

