import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.node.models import Node
from apps.node_activity.models import ActiveNode

#disable node from dashboard
from apps.notice.models import Notice

channel_layer = get_channel_layer()

@receiver(post_save,sender=Node)
def disable_node(sender,instance,**kwargs):

    if instance.status=='disable':
        try:
            active_node=ActiveNode.objects.get(node=instance.node_id)
            async_to_sync(channel_layer.group_send)(active_node.single_group,{'type':'discard_single_node','action':'disconnect'})
        except:
            pass



 
@receiver(post_save,sender=Notice)
def send_notice(sender,instance,**kwargs):
    if instance.status=='published':
        async_to_sync(channel_layer.group_send)('public',{
            'type':'send_notice',
            'notice':json.dumps({'title':instance.title,'body':instance.body}),
        })

