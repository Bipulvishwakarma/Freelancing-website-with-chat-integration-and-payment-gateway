from django.urls import re_path
from . import consumers
from django.urls import path
from enroll.consumers import ChatConsumer
from channels.routing import URLRouter

websocket_urlpatterns = [
    re_path(r'^ws/(?P<room_name>[^/]+)/$',consumers.ChatConsumer.as_asgi()),
]