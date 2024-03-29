from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse_lazy
from apps.school.models import School




class Teacher(models.Model):
    name       = models.CharField(max_length=30)
    image      = models.ImageField(upload_to='teacher',default='default.png')
    teacher_id = models.AutoField(primary_key=True,unique=True)
    designation= models.CharField(max_length=20)
    school_id  = models.ForeignKey(School,on_delete=models.DO_NOTHING)
    school_name =models.CharField(max_length=100)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-created']

    def get_absolute_url(self):
        return reverse_lazy('teacher:teacher_detail',kwargs={'pk':self.pk})

@receiver(pre_save,sender=Teacher)
def pre_save_school_name(sender,instance,**kwargs):
    instance.school_name = instance.school_id.name




