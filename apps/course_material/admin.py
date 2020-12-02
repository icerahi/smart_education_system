from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite
from import_export.admin import ImportExportModelAdmin

from apps.course_material.models import Class, Subject, Unit, CourseMaterial


@admin.register(Class)
class ClassAdmin(ImportExportModelAdmin):
    list_display = ('name',)

@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    list_filter = ('class_name__name',)

@admin.register(Unit)
class UnitAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    list_filter = ('class_name__name','subject__name',)

@admin.register(CourseMaterial)
class CourseMaterialAdmin(ImportExportModelAdmin):
    list_display = ('class_name','subject','unit','content')
    list_filter = ('class_name__name','subject__name','unit__name',)


