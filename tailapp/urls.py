from django.urls import path
from .views import health, message_window

urlpatterns = [path("health/", health), path("messages/", message_window)]
