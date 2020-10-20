from django.contrib import admin
from django.apps import apps
from .models import District, Division, Upazila, Union,School
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Union
class UnionResource(resources.ModelResource):
    class Meta:
        model = Union
@admin.register(Union)
class UnionAdmin(ImportExportModelAdmin):
    pass

# Upazila
class UpazilaResource(resources.ModelResource):
    class Meta:
        model = Upazila
@admin.register(Upazila)
class UpazilaAdmin(ImportExportModelAdmin):
    pass

#District
class DistrictResource(resources.ModelResource):
    class Meta:
        model = District
@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    pass

#Division
class DivisionResource(resources.ModelResource):
    class Meta:
        model = Division
@admin.register(Division)
class DivisionAdmin(ImportExportModelAdmin):
    pass

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}



admin.site.site_title = "Smart Education System"
admin.site.site_header = "Smart Education System"
admin.site.site_index_title = "Smart Education System"

