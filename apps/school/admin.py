from django.contrib import admin

# Register your models here.
from .models import District, Division, Upazila, Union,School
from import_export import resources
from import_export.admin import ImportExportModelAdmin

################# model Register with import_export module #####################
# Union
class UnionResource(resources.ModelResource):
    class Meta:
        model = Union
@admin.register(Union)
class UnionAdmin(ImportExportModelAdmin):
    list_display = ('name','upazila','district','division')
    list_filter = ('upazila__district__name',)


# Upazila
class UpazilaResource(resources.ModelResource):
    class Meta:
        model = Upazila
@admin.register(Upazila)
class UpazilaAdmin(ImportExportModelAdmin):
    list_display = ('name','district','division')
    list_filter = ('district__name',)

#District
class DistrictResource(resources.ModelResource):
    class Meta:
        model = District

@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    list_display = ('name','division')
    list_filter = ('division__name',)

#Division
class DivisionResource(resources.ModelResource):
    class Meta:
        model = Division
@admin.register(Division)
class DivisionAdmin(ImportExportModelAdmin):
    pass
###########################################################


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    search_fields = ['name']

