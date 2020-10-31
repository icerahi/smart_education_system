from django.forms import ModelForm

from apps.teacher.models import Teacher


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('name','image','designation','school_id',)

    def __init__(self,*args,**kwargs):
        super(TeacherForm, self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['designation'].widget.attrs['class'] = 'form-control'
        self.fields['school_id'].widget.attrs['class'] = 'form-control'




