import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import routing

#from routing import websocket_urlpatterns  # Импортируй URL-шаблоны WebSocket

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
           # routing.websocket_urlpatterns
        )
    ),
})