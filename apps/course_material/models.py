import os

from django.db import models

# Create your models here.
from django.urls import reverse_lazy

from smart_selects.db_fields import ChainedForeignKey


class Class(models.Model):
    name = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "   Classes"

class Subject(models.Model):
    class_name = models.ManyToManyField(Class)
    name       = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "  Subjects"

class Chapter(models.Model):
    class_name = models.ManyToManyField(Class)
    subject = models.ManyToManyField(Subject)
    name        = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = " Chapters"

#FILE   STORING
def content_file_name(instance,filename):
    ext = filename.split('.')[-1]
    filename=f'chapter_{instance.chapter.name}.'+ext
    return os.path.join(f'course_material/class_{instance.class_name.name}/{instance.subject.name}/chapter_{instance.chapter.name}/'+str(filename))

class CourseMaterial(models.Model):
    class_name   = models.ForeignKey(Class,on_delete=models.CASCADE)
    subject  = ChainedForeignKey(Subject,chained_field='class_name',chained_model_field='class_name',
                                     show_all=False,auto_choose=True,sort=True)
    chapter  = ChainedForeignKey(Chapter,chained_field='subject',chained_model_field='subject',
                                     show_all=False,auto_choose=True,sort=True)
    title   = models.TextField()
    content  = models.FileField(upload_to=content_file_name)

    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)



    def get_edit_url(self):
        return reverse_lazy('course_material:update_content',kwargs={'class_name':self.class_name.name,
                                                                     'subject':self.subject.name,
                                                                     'chapter':self.chapter.name,
                                                                     'pk':self.pk})

     

    def __str__(self):
        return f'content of {self.chapter.name}'

    class Meta:
        #class_name,subject,chapter can't be multiple,all least one field below need to be non same.
        ordering=['-created']
        constraints =[
            models.UniqueConstraint(
                fields=['class_name','subject','chapter'],
                name = 'unique content'
            )
        ]
        verbose_name_plural = "CourseMeterials"

