from django.contrib import admin

# Register your models here.
from apps.class_routine.models import Routine, Day


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    pass

@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('class_name','subject','day','start_time','end_time')
    list_filter = ('start_time','class_name')


