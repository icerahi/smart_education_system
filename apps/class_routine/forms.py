from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models import F, Q
from django.forms import ModelForm
from django import forms

from apps.class_routine.models import Routine


class RoutineForm(ModelForm):
    #for time input widget
    start_time = forms.CharField(required=True,widget=forms.TimeInput(attrs={
        'type':'time',
        'class':'form-control'
    }))

    end_time = forms.CharField(required=True,widget=forms.TimeInput(attrs={
        'type':'time',
        'class':'form-control'
    }))


    class Meta:
        model = Routine
        fields = ('class_name','subject','day','start_time','end_time',)

    def __init__(self,*args,**kwargs):
        super(RoutineForm, self).__init__(*args,**kwargs)
        self.fields['class_name'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['day'].widget.attrs['class'] = 'form-control'

    def clean(self):
        class_name = self.cleaned_data['class_name']
        subject = self.cleaned_data['subject']
        day = self.cleaned_data['day']
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']

        if Routine.objects.filter(Q(class_name=class_name) & Q(day=day) & Q(start_time__range=(start_time,end_time))).exists():
            raise ValidationError('Subject in this time range of day is already exists!')
        if Routine.objects.filter(Q(class_name=class_name) & Q(day=day) & Q(end_time__range=(start_time,end_time))).exists():
            raise ValidationError('Subject in this time range of day is already exists!')
        return super(RoutineForm, self).clean()
