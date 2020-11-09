
from ckeditor.fields import RichTextField,RichTextFormField
from django.db import models

# Create your models here.



class Notice(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Publish Now'),
        ('archived','Archived')
    )
    title = models.CharField(max_length=250)
    body  = RichTextField()
    status = models.CharField(max_length=12,choices=STATUS_CHOICES,default='draft')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


