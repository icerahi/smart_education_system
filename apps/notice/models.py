from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from ckeditor.fields import RichTextField,RichTextFormField
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver



class Notice(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived','Archived')
    )
    title = models.CharField(max_length=250)
    body  = RichTextField()
    status = models.CharField(max_length=12,choices=STATUS_CHOICES,default='draft')

    published = models.BooleanField(default=False)
    archived  = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    class Meta:
        ordering=["-updated"]
    def __str__(self):
        return self.title

@receiver(pre_save,sender=Notice)
def pre_save_status(sender,instance,**kwargs):
    if instance.status == 'draft':
        instance.published = False
        instance.archived = False
    if instance.status == 'published':
       instance.published=True
    if instance.status == 'archived':
        instance.archived = True

