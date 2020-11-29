from django.contrib import admin

# Register your models here.
from apps.node.models import Node


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('ip_address','port','node_id','mac_address','school_id','school_name','class_name','status',)
    prepopulated_fields = {'slug':['school_name','class_name'],'school_name':['school_id']}
    list_editable = ('status',)
