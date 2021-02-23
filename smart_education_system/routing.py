from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from apps.node_activity import routing


application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(URLRouter(routing.websocket_urlpattern))
})