from django.contrib import admin

# Register your models here.
from apps.notice.models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    pass
