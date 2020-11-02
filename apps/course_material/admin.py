from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite

from apps.course_material.models import Class, Subject, Chapter, CourseMaterial


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('_class__name',)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('_class__name','subject__name',)

@admin.register(CourseMaterial)
class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = ('_class','subject','chapter','content')
    list_filter = ('_class__name','subject__name','chapter__name',)


