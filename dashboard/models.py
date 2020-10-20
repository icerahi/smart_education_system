from django.db import models
import uuid
# Create your models here.
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify


class Division(models.Model):
    name   = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return f'{self.name}'

class District(models.Model):
    name    = models.CharField(max_length=50,unique=True)
    division= models.ForeignKey(Division,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}-{self.division.name}'

class Upazila(models.Model):
    name    = models.CharField(max_length=50)
    district= models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}-{self.district.name}'

class Union(models.Model):
    name = models.CharField(max_length=50)
    upazila = models.ForeignKey(Upazila,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}-{self.upazila.name}-{self.upazila.district.name}'

class School(models.Model):
    name        = models.CharField(max_length=300)
    school_id   = models.AutoField(primary_key=True)
    slug        = models.SlugField()
    division    = models.ForeignKey(Division,on_delete=models.CASCADE)
    district    = models.ForeignKey(District,on_delete=models.CASCADE)



def save_post(sender,instance,**kwargs):
    print("Post save signal working")
post_save.connect(save_post,sender=School)

@receiver(pre_save,sender=School)
def pre_save_slug(sender,instance,**kwargs):
    instance.slug = slugify(instance.name)
    print(instance)
    # print("working")
    # slug=slugify(kwargs['instance'].name)
    # kwargs['instance'].slug=slug

""">>> div = Division.objects.get(id=1)
>>> dis = div.district_set.all()
"""


