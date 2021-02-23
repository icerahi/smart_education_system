from django.contrib import admin

# Register your models here.
from apps.node_activity.models import ActiveNode


@admin.register(ActiveNode)
class ActiveNodeAdmin(admin.ModelAdmin):
    list_display = ('node','group_name','single_group','channel_name')

