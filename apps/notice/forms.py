from django.forms import ModelForm

from apps.notice.models import Notice


class NoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields =('title','body','status')


    def __init__(self,*args,**kwargs):
        super(NoticeForm, self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['body'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
