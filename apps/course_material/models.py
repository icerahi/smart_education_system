import os

from django.db import models

# Create your models here.
from django.urls import reverse_lazy

from smart_selects.db_fields import ChainedForeignKey


class Class(models.Model):
    name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "   Classes"

class Subject(models.Model):
    class_name = models.ManyToManyField(Class)
    name       = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "  Subjects"

class Unit(models.Model):
    class_name = models.ManyToManyField(Class)
    subject = models.ManyToManyField(Subject)
    name        = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = " Units"

#FILE   STORING
def content_file_name(instance,filename):
    ext = filename.split('.')[-1]
    filename=f'unit_{instance.unit.name}.'+ext
    return os.path.join(f'course_material/class_{instance.class_name.name}/{instance.subject.name}/unit_{instance.unit.name}/'+str(filename))

class CourseMaterial(models.Model):
    class_name   = models.ForeignKey(Class,on_delete=models.CASCADE)
    subject  = ChainedForeignKey(Subject,chained_field='class_name',chained_model_field='class_name',
                                     show_all=False,auto_choose=True,sort=True)
    unit  = ChainedForeignKey(Unit,chained_field='subject',chained_model_field='subject',
                                     show_all=False,auto_choose=True,sort=True)

    unit_name =  models.TextField()
    content  = models.FileField(upload_to=content_file_name)

    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)



    def get_edit_url(self):
        return reverse_lazy('course_material:update_content',kwargs={'class_name':self.class_name.name,
                                                                     'subject':self.subject.name,
                                                                     'unit':self.unit.name,
                                                                     'pk':self.pk})

     

    def __str__(self):
        return f' {self.unit.name}'

    class Meta:
        #class_name,subject,unit can't be multiple,all least one field below need to be non same.
        ordering=['-created']
        constraints =[
            models.UniqueConstraint(
                fields=['class_name','subject','unit'],
                name = 'unique content'
            )
        ]
        verbose_name_plural = "CourseMeterials"

