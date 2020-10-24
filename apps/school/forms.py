from django.forms import ModelForm
from related_select.fields import RelatedChoiceField

from apps.school.models import School


class SchoolCreateForm(ModelForm):

    class Meta:
        model = School
        fields =('name','division','district','upazila',
                 'union','village')

    def __init__(self,*args,**kwargs):
        super(SchoolCreateForm, self).__init__(*args,**kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['division'].widget.attrs['class'] = 'form-control'
        self.fields['district'].widget.attrs['class'] = 'form-control'
        self.fields['upazila'].widget.attrs['class'] = 'form-control'
        self.fields['union'].widget.attrs['class'] = 'form-control'
        self.fields['village'].widget.attrs['class'] = 'form-control'

