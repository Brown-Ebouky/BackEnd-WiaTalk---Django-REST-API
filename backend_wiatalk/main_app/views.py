from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
     A  view set for the users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ChatViewSet(viewsets.ModelViewSet):
    """
     A  view set for the chats
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class GroupChatViewSet(viewsets.ModelViewSet):
    """
     A  view set for the groupChats
    """
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatSerializer

class MessageViewSet(viewsets.ModelViewSet):
    """
     A  view set for the messages
    """
    queryset = Message.objects.all()
    serializer_class = GroupChatSerializer

class GroupMessageViewSet(viewsets.ModelViewSet):
    """
     A  view set for the groupMessages
    """
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageSerializer

class CallViewSet(viewsets.ModelViewSet):
    """
     A  view set for the calls
    """
    queryset = Call.objects.all()
    serializer_class = CallSerializer

class GroupCallViewSet(viewsets.ModelViewSet):
    """
     A  view set for the group calls
    """
    queryset = GroupCall.objects.all()
    serializer_class = GroupCallSerializer