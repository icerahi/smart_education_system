from django.db import models

# Create your models here.
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse_lazy, reverse


from smart_selects.db_fields import ChainedForeignKey



class Division(models.Model):
    name   = models.CharField(verbose_name="Division",max_length=50,unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "    Divisions"

class District(models.Model):
    name    = models.CharField(verbose_name="District",max_length=50,unique=True)
    division= models.ForeignKey(Division,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "   Districts"

class Upazila(models.Model):
    name    = models.CharField(verbose_name="Upazila",max_length=50)
    district= models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "  Upazilas"

    #displaying foriegnkey name for admin
    def get_division(self):
        return self.district.division.name
    division = property(get_division)

class Union(models.Model):
    name = models.CharField(verbose_name="Union",max_length=50)
    upazila = models.ForeignKey(Upazila,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = " Unions"

    #displaying foreignkey name for admin
    def get_district(self):
        return self.upazila.district.name
    def get_division(self):
        return self.upazila.district.division.name
    district = property(get_district)
    division = property(get_division)



class School(models.Model):
    name        = models.CharField(max_length=100)
    school_id   = models.AutoField(primary_key=True,unique=True)
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
        return str(self.school_id)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Schools"

    def get_absolute_url(self):
        return reverse_lazy('school:school_detail',kwargs={'pk':self.pk,})





