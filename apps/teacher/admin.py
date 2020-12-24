from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from apps.teacher.models import Teacher

@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin):
    list_display = ('name','teacher_id','school_id','school_name')
    prepopulated_fields = {'school_name':['school_id']}
