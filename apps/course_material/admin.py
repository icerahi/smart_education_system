from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite

from apps.course_material.models import Class, Subject, Chapter, CourseMaterial


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name','class_name',)
    list_filter = ('class_name__name',)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name','subject_name','class_name',)
    list_filter = ('class_name__name','subject_name__name',)

@admin.register(CourseMaterial)
class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = ('class_name','subject_name','chapter_name','content')
    list_filter = ('class_name__name','subject_name__name','chapter_name__name',)


