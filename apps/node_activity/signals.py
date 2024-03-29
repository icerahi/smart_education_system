import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import request

from apps.course_material.models import CourseMaterial
from apps.node.models import Node
from apps.node_activity.consumers import server_ip_address
from apps.node_activity.models import ActiveNode

#disable node from dashboard
from apps.notice.models import Notice
from apps.school.models import School

channel_layer = get_channel_layer()

@receiver(post_save,sender=Node)
def disable_node(sender,instance,**kwargs):

    if instance.status=='disable':
        try:
            active_node=ActiveNode.objects.get(node=instance.node_id)
            async_to_sync(channel_layer.group_send)(active_node.single_group,{'type':'disable_single_node','data':json.dumps({'action':'disable'})})
        except:
            pass



###COURSE MATERIAL REALTIME NOT NEED IT WILL MAKE HASSLE ,ALL CONTENT WILL GET WHEN NOODE RESTART
@receiver(post_save,sender=CourseMaterial)
def send_course_material(sender,instance,created,**kwargs):
    try:
        async_to_sync(channel_layer.group_send)(f'class_group_{instance.class_name.name}',
                                                {
                                                    'type':'send_course_material',
                                                    'data':json.dumps({'course_material':{"content_id":instance.id,
                                                                                          "class_name":instance.class_name.name,
                                                                                          "subject":instance.subject.name,
                                                                                          "unit":instance.unit.name,
                                                                                          "unit_name":instance.unit_name,
                                                                                          "content":server_ip_address()+":8000"+instance.content.url}})
                                                })
    except:
        pass
 
@receiver(post_save,sender=Notice)
def send_notice(sender,instance,**kwargs):
    if instance.status=='published':
        try:
            async_to_sync(channel_layer.group_send)('public',{
                'type':'send_notice',
                'data':json.dumps({'notice':{'title':instance.title,'body':instance.body}}),
            })
        except:
            pass




@receiver(post_save,sender=School)
def post_save_and_school_name(sender,instance,**kwargs):
    try:
        nodes=Node.objects.filter(school_id=instance.school_id)
        for node in nodes:
            node.school_name = instance.name
            node.save()
    except:
        pass