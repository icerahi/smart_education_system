from django.urls import path

from apps.node_activity import consumers

websocket_urlpattern=[
    path('ws/connect/',consumers.NodeConsumer.as_asgi()),

   # path('ws/test_connection/',consumers.TestConnectionConsumer.as_asgi())
]