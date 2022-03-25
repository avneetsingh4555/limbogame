from asyncio.windows_events import NULL
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Player
# from .models import Message

class GameConsumer(AsyncWebsocketConsumer):
    global test

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    # Receive message from web socket
    async def receive(self, text_data):
        data = json.loads(text_data)
        score = data['score']
        username = data['username']
        room = data['room']
        
        currentuser = data['currentuser']
        picda = data['picda']
        lastcard = data['lastcard']
        dropcards = data['dropcards']
        # doubleproperty = data['doubleproperty']
        print(currentuser)
        if(picda != 0):
            lastcard=picda

        
        if (int(currentuser)==1):
            currentuser = int(currentuser) + 1
        else:
            currentuser=  int(currentuser) - 1

        print(room)
       
        dropcards=await self.save_message(currentuser,room,picda,lastcard)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'score': score,
                'username': username,
                'currentuser': currentuser,
                'picda': picda,
                'lastcard': lastcard,
                'dropcards': dropcards,
                # 'doubleproperty': doubleproperty,
            }
        )
    
    # Receive message from room group
    async def chat_message(self, event):
        score = event['score']
        username = event['username']
        currentuser = event['currentuser']
        picda = event['picda']
        lastcard = event['lastcard']
        dropcards = event['dropcards']
        # doubleproperty = event['doubleproperty']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'score': score,
            'username': username,
            'currentuser': currentuser,
            'picda': picda,
            'lastcard': lastcard,
            'dropcards': dropcards,
            # 'doubleproperty': doubleproperty,
        }))

    @sync_to_async
    def save_message(self,currentuser,room,picda,lastcard):
        if lastcard != 0 and picda !=0:
            w1 = Player.objects.filter(roomid=room)
            
            old_used_cards=w1[0].used_cards
            usedcards=''

            if not old_used_cards:
                usedcards=picda
            else:
                usedcards=old_used_cards+','+picda    

            dropcards=usedcards    
            

            w1 = Player.objects.filter(roomid=room).update(
            used_cards=usedcards)

            return dropcards 
        