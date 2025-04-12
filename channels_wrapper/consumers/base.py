from channels.generic.websocket import AsyncWebsocketConsumer
import json

class BaseConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message":"Connected via websocket"}))
        
    async def receive(self, text_data=None, bytes_data=None):
        await self.send(text_data=json.dumps({"echo": text_data}))
        return await super().receive(text_data, bytes_data)