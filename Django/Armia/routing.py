from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import Armia.routing  # Замените 'Armia' на имя вашего приложения
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/some_path/', consumers.YourWebSocketConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            Armia.routing.websocket_urlpatterns
        )
    ),
})