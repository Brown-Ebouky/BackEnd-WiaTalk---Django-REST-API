"""backend_wiatalk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'chats', ChatViewSet, basename='chat')
router.register(r'groupchats', GroupChatViewSet, basename='groupchat')
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'groupmessages', GroupMessageViewSet, basename='groupmessage')
router.register(r'calls', CallViewSet, basename='call')
router.register(r'groupcalls', GroupCallViewSet, basename='groupcall')


urlpatterns = router.urls
