from channels.generic.websocket import AsyncWebsocketConsumer
import json

class BaseConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print(f"Connected with channel name: {self.channel_name}")
        await self.send(text_data="Connected to WebSocket!")
        
    async def disconnect(self, code):
        return await super().disconnect(code)
    
    async def receive(self, text_data):
        await self.send(text_data=f"You said: {text_data}")