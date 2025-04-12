from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data="Connected to WebSocket!")

    async def disconnect(self, close_code):
        print("WebSocket disconnected.")

    async def receive(self, text_data):
        await self.send(text_data=f"You said: {text_data}")
