import os

from django.db import models

# Create your models here.
from smart_selects.db_fields import ChainedForeignKey


class Class(models.Model):
    name = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "   Classes"

class Subject(models.Model):
    _class = models.ManyToManyField(Class)
    name       = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "  Subjects"

class Chapter(models.Model):
    _class = models.ManyToManyField(Class)
    subject = models.ManyToManyField(Subject)
    name        = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = " Chapters"

#FILE   STORING
def content_file_name(instance,filename):
    ext = filename.split('.')[-1]
    print(ext)
    filename=f'chapter_{instance.chapter.name}.'+ext
    print(filename)
    return os.path.join(f'course_material/class_{instance._class.name}/{instance.subject.name}/chapter_{instance.chapter.name}/'+str(filename))

class CourseMaterial(models.Model):
    _class = models.ForeignKey(Class,on_delete=models.CASCADE)
    subject = ChainedForeignKey(Subject,chained_field='_class',chained_model_field='_class',
                                     show_all=False,auto_choose=True,sort=True)
    chapter = ChainedForeignKey(Chapter,chained_field='subject',chained_model_field='subject',
                                     show_all=False,auto_choose=True,sort=True,unique=True)
    content     = models.FileField(upload_to=content_file_name,unique=True)

    def __str__(self):
        return f'content of {self.chapter.name}'

    class Meta:
        verbose_name_plural = "CourseMeterials"