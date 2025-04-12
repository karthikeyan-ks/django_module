import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

from channels_wrapper.routing import websocket_urlpatterns  # ✅ Make sure this import is correct

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # ✅ Your WebSocket routes go here
        )
    ),
})
