from django.urls import re_path

from .consumers import MessageConsumer

websocket_urlpatterns = [
    re_path(r"ws/get-messages/$", MessageConsumer.as_asgi()),
]