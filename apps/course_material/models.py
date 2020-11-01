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
    class_name = models.ForeignKey(Class,on_delete=models.CASCADE)
    name       = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "  Subjects"
class Chapter(models.Model):
    class_name = models.ForeignKey(Class,on_delete=models.CASCADE)
    subject_name = ChainedForeignKey(Subject,chained_field='class_name',chained_model_field='class_name',
                                     show_all=False,auto_choose=True,sort=True)
    name        = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = " Chapters"

#FILE   STORING
def content_file_name(instance,filename):
    ext = filename.split('.')[-1]
    print(ext)
    filename=f'chapter_{instance.chapter_name.name}.'+ext
    print(filename)
    return os.path.join(f'course_material/class_{instance.class_name.name}/{instance.subject_name.name}/chapter_{instance.chapter_name.name}/'+str(filename))

class CourseMaterial(models.Model):
    class_name = models.ForeignKey(Class,on_delete=models.CASCADE)
    subject_name = ChainedForeignKey(Subject,chained_field='class_name',chained_model_field='class_name',
                                     show_all=False,auto_choose=True,sort=True)
    chapter_name = ChainedForeignKey(Chapter,chained_field='subject_name',chained_model_field='subject_name',
                                     show_all=False,auto_choose=True,sort=True)
    content     = models.FileField(upload_to=content_file_name,unique=True)

    def __str__(self):
        return f'content of {self.chapter_name.name}'

    class Meta:
        verbose_name_plural = "CourseMeterials"