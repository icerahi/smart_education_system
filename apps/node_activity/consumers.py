from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async

from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.exceptions import ObjectDoesNotExist


from apps.node.models import Node
import json

from apps.node_activity.models import ActiveNode

#active node delete function
def delete_node(channel_name):
    return ActiveNode.objects.get(channel_name=channel_name).delete()

def get_class_name(node):
     return node.class_name.name

class NodeConsumer(AsyncWebsocketConsumer):
    group_name= "public"

    async def connect(self):
        self.ip_address = self.scope['client'][0]

        try:
            #check the connect node if available if Node Model
            self.node = await sync_to_async(Node.objects.get)(ip_address=self.ip_address)


            # if node id exists then accept connection & add it into group
            if (self.node and self.node.status=='enable'):# checking is node exists and status enable
                await self.accept()
                await self.channel_layer.group_add(self.group_name, self.channel_name)

                self.single_group = f'node_{self.node.node_id}' #single group
                await self.channel_layer.group_add(self.single_group,self.channel_name)

                #get node data from Node data by filtering it's ip address
                #we create 'get_class_name' function cz in await sync_to_async query for foreignkey not working.
                self.class_name =await  sync_to_async(get_class_name)(self.node)
                self.node_data = json.dumps({'node_data':{'node_id':self.node.node_id,
                                             'ip_address':self.node.ip_address,
                                             'school_name':self.node.school_name,
                                             'class_name':self.class_name,
                                             }})

                #add connected Node to ActiveModel
                await sync_to_async(ActiveNode.objects.create)(node=self.node,group_name=self.group_name,
                                          single_group=self.single_group,channel_name=self.channel_name)

                #send node data to specafic node by one to one communication
                await self.channel_layer.group_send(self.single_group,{
                    'type':'send_node_data',
                    'data':self.node_data,
                })
        except :
            raise  DenyConnection("Invalid Authentication")
            await self.close()


    async def disconnect(self,code):

        try:
            #get node from ActiveNode Model
            self.node = await sync_to_async(ActiveNode.objects.get)(channel_name=self.channel_name)
            #node remove from group before disconnect
            # await self.channel_layer.group_discard(self.group_name, self.channel_name)
            # await self.channel_layer.group_discard(self.single_group, self.channel_name)

            #delete node object from ActiveNode when disconnect
            await sync_to_async(delete_node)(self.channel_name) #call delete_node function from above
            await self.close()
        except ObjectDoesNotExist:
            await self.close()

    async  def receive(self,text_data=None):
        print("###",text_data)


    async def disable_single_node(self,event):
        data = json.loads(event['data'])
        if 'action' in data and data['action'] == 'disable':
            return await self.close()

    async def send_node_data(self,event):
        await self.send(event['data'])

    async def send_notice(self,event):
        await self.send(event['data'])


