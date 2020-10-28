from django.db import models

# Create your models here.
from smart_selects.db_fields import ChainedForeignKey

from apps.school.models import School


class Teacher(models.Model):
    name       = models.CharField(max_length=30)
    image      = models.ImageField(upload_to='teacher',default='default.png')
    teacher_id = models.AutoField(primary_key=True)
    designation= models.CharField(max_length=20)
    school_id  = models.ForeignKey(School,to_field='school_id',on_delete=models.DO_NOTHING)

    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

