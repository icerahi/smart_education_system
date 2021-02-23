from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from apps.notice.models import Notice


@admin.register(Notice)
class NoticeAdmin(ImportExportModelAdmin):
    list_display = ('title','status','updated')
    list_filter = ('status',)
