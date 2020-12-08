from django.shortcuts import render

# Create your views here.

class TestConnectionConsumer(AsyncWebsocketConsumer):
    group_name = 'sms'
    async def connect(self):
        self.ip = self.scope['client'][0]
        print('tryied to connect',self.ip)


        try:
            self.node =await  sync_to_async(Node.objects.get)(ip_address=self.ip)

            if (self.node and self.node.status=='enable'):
                print("Online :",self.ip)
                self.data=json.dumps({'node_id':self.node.node_id,'node ip':self.node.ip_address,
                                 'school name':self.node.school_name})
                await self.channel_layer.group_add(self.group_name, self.channel_name)
                await self.accept()
                #need to implement one to one communication for indivisual unique message
                # await self.channel_layer.group_send(self.group_name,
                #                     {'type': 'hello', 'data':self.data})



        except ObjectDoesNotExist:
            raise DenyConnection("Invalid Authentication")


    async def disconnect(self,code):
        self.ip = self.scope['client'][0]
        print("Offline :",self.ip)

        await self.channel_layer.group_discard(self.group_name,self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        print(">>>",text_data)


    async def hello(self,event):
        print(event)
        await self.send(event['data'])


