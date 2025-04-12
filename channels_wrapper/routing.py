from django.urls import path
from channels_wrapper.consumers.base import BaseConsumer
from channels_wrapper.consumers.test import TestConsumer
from channels_wrapper.consumers.chat.base import BaseConsumer as ChatBaseConsumer

websocket_urlpatterns = [
    path("ws/base/", BaseConsumer.as_asgi()),
    path("ws/test/", TestConsumer.as_asgi()),
    path("ws/chat/", ChatBaseConsumer.as_asgi())
]
