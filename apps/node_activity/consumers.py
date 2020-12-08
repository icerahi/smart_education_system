from asgiref.sync import sync_to_async

from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.exceptions import ObjectDoesNotExist


from apps.node.models import Node
import json

from apps.node_activity.models import ActiveNode

#active node delete function
def delete_node(channel_name):
    ActiveNode.objects.get(channel_name=channel_name).delete()

def node_filter(ip_address):
    ActiveNode.objects.filter(ip_address=ip_address).exists()

class NodeConsumer(AsyncWebsocketConsumer):
    group_name= "public"

    async def connect(self):
        self.ip_address = self.scope['client'][0]



        try:
            self.node = await sync_to_async(Node.objects.get)(ip_address=self.ip_address)
            # if node id exists then accept connection & add it into group

            if (self.node and self.node.status=='enable'):
                await self.accept()
                await self.channel_layer.group_add(self.group_name, self.channel_name)

                self.single_group = f'node_{self.node.node_id}' #single group
                await self.channel_layer.group_add(self.single_group,self.channel_name)

                self.node_data = json.dumps({'node_id':self.node.node_id,
                                             'ip_address':self.node.ip_address,
                                             'school_name':self.node.school_name,
                                             })

                #add to active model
                await sync_to_async(ActiveNode.objects.create)(node=self.node,group_name=self.group_name,
                                          single_group=self.single_group,channel_name=self.channel_name)

                await self.channel_layer.group_send(self.single_group,{
                    'type':'send_node_data',
                    'node_data':self.node_data,
                })
        except:
            raise  DenyConnection("Invalid Authentication")
            await self.close()


    async def disconnect(self,code):
        try:
            self.node = await sync_to_async(ActiveNode.objects.get)(channel_name=self.channel_name)

            await self.channel_layer.group_discard(self.group_name, self.channel_name)
            await self.channel_layer.group_discard(self.single_group, self.channel_name)

            await sync_to_async(delete_node)(self.channel_name) #call delete_node function from above

        except ObjectDoesNotExist:
            await self.close()




    async  def receive(self,text_data=None):
        print("###",text_data)

    async def send_node_data(self,event):
        print(event['node_data'])
        await self.send(event['node_data'])
