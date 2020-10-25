from django.db import models

# Create your models here.
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from smart_selects.db_fields import ChainedForeignKey


class Division(models.Model):
    name   = models.CharField(verbose_name="Division",max_length=50,unique=True)

    def __str__(self):
        return f'{self.name}'

class District(models.Model):
    name    = models.CharField(verbose_name="District",max_length=50,unique=True)
    division= models.ForeignKey(Division,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'

class Upazila(models.Model):
    name    = models.CharField(verbose_name="Upazila",max_length=50)
    district= models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    #displaying foriegnkey name for admin
    def get_division(self):
        return self.district.division.name
    division = property(get_division)

class Union(models.Model):
    name = models.CharField(verbose_name="Union",max_length=50)
    upazila = models.ForeignKey(Upazila,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    #displaying foreignkey name for admin
    def get_district(self):
        return self.upazila.district.name
    def get_division(self):
        return self.upazila.district.division.name
    district = property(get_district)
    division = property(get_division)



class School(models.Model):
    name        = models.CharField(max_length=300)
    school_id   = models.AutoField(primary_key=True)
    slug        = models.SlugField()
    division    = models.ForeignKey(Division,on_delete=models.CASCADE)
    district    = ChainedForeignKey(District,chained_field='division',chained_model_field='division',
                                    show_all=False,auto_choose=True,sort=True)
    upazila     = ChainedForeignKey(Upazila,chained_field='district',chained_model_field='district',
                                    show_all=False,auto_choose=True,sort=True)
    union       = ChainedForeignKey(Union,chained_field='upazila',chained_model_field='upazila',
                                    show_all=False,auto_choose=True,sort=True)
    village     = models.CharField(max_length=50)
   #image       = models.ImageField(upload_to='school',default)

    created     =models.DateTimeField(auto_now_add=True)
    updated     =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse_lazy('school:school_detail',kwargs={'pk':self.pk,'slug':self.slug})

    def get_delete_url(self):
        return reverse_lazy('school:school_delete',kwargs={'pk':self.pk,'slug':self.slug})

    def get_update_url(self):
        return reverse_lazy('school:school_update',kwargs={'pk':self.pk,'slug':self.slug})

@receiver(pre_save,sender=School)
def pre_save_slug(sender,instance,**kwargs):
   instance.slug = slugify(instance.name)




