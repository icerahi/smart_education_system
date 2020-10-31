from django.contrib import admin

# Register your models here.
from apps.teacher.models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name','teacher_id','school_id','school_name')
    prepopulated_fields = {'slug':['name'],'school_name':['school_id']}
