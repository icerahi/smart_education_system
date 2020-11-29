from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from apps.school.models import School


class Node(models.Model):
    STATUS_CHOICES = (
        ('enable', 'Enable'),
        ('disable', 'Disable'),

    )
    node_id     = models.AutoField(primary_key=True)
    ip_address  = models.GenericIPAddressField()
    port        = models.IntegerField(null=True,blank=True)
    mac_address = models.CharField(max_length=50,null=True,blank=True)
    school_id     = models.ForeignKey(School,on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    class_name  = models.CharField(max_length=15,unique=True)
    slug        = models.SlugField()
    status      = models.CharField(max_length=15,choices=STATUS_CHOICES,default='disable')


    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.node_id)

    class Meta:
        ordering = ['-created']


@receiver(pre_save,sender=Node)
def pre_save_slug_and_school_name(sender,instance,**kwargs):
    instance.school_name = instance.school_id.name
    instance.slug  = slugify(instance.school_name+f'-{instance.class_name}')