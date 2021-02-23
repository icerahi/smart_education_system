from django.db import models

# Create your models here.
from apps.node.models import Node

 

class ActiveNode(models.Model):
    node = models.OneToOneField(Node,on_delete=models.CASCADE,)
    group_name = models.CharField(max_length=20)
    single_group = models.CharField(max_length=30)
    class_group  = models.CharField(max_length=30,null=True,blank=True)
    channel_name = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        # constraints =[
        #     models.UniqueConstraint(
        #         fields=['node','single_group','channel_name'],
        #         name = 'Connect Unique Node'
        #     )
        # ]
        # verbose_name_plural = "CourseMeterials"
