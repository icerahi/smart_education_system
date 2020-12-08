from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.node.models import Node
from apps.node_activity.models import ActiveNode


@receiver(post_save,sender=Node)
def disable_node(sender,instance,**kwargs):
    if instance.status=='disable':
        try:
            active_node=ActiveNode.objects.get(id=instance)
            if active_node:
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_discard)(active_node.group_name,active_node.channel_name)
                async_to_sync(channel_layer.group_discard)(active_node.single_group,active_node.channel_name)
        except:
            pass

