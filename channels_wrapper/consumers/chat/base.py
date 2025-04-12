from channels.generic.websocket import AsyncWebsocketConsumer
import json

class BaseConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print(f"Connected with channel name: {self.channel_name}")
        
        
    async def disconnect(self, code):
        return await super().disconnect(code)