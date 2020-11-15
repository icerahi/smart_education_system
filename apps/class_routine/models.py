from django.db import models

# Create your models here.
from django.db.models import Q
from smart_selects.db_fields import ChainedForeignKey

from apps.course_material.models import Class, Subject

class Day(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name



class Routine(models.Model):
    class_name = models.ForeignKey(Class,on_delete=models.CASCADE)
    subject    = ChainedForeignKey(Subject,chained_field='class_name',chained_model_field='class_name',
                                   show_all=False,auto_choose=True,sort=True)
    day       = models.ForeignKey(Day,on_delete=models.CASCADE)

    start_time  = models.TimeField()
    end_time    = models.TimeField()


    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.class_name.name

    class Meta:
        ordering =['start_time']

        constraints = [
            models.UniqueConstraint(
                fields=['class_name', 'subject', 'day',],
                name='unique data with class_name subject and day'
            ),
            ]
