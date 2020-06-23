from rest_framework import serializers
from .models import User, Chat, GroupChat, Message, GroupMessage, Call, GroupCall

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'sipIdentifier', 'online', 'classe', 'photoUrl']

class ChatSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model: Chat
        fields: ['user']

class GroupChatSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model: GroupChat
        fields: ['title', 'users']

class MessageSerializer(serializers.ModelSerializer):
    user_1 = UserSerializer()
    user_2 = UserSerializer()
    chat = ChatSerializer()

    class Meta:
        model: Message
        fields: ['timestamp', 'messageText', 'video', 'photo', 'audio', 'recieved', 'seen', 'user_1', 'user_2', 'chat']


class GroupMessageSerializer(serializers.ModelSerializer):
    groupChat = GroupChatSerializer()
    users_rec = UserSerializer(many=True)
    users_seen = UserSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model: GroupMessage
        fields: ['timestamp', 'messageText', 'video', 'photo', 'audio', 'groupChat', 'user', 'users_rec', 'users_seen']

class CallSerializer(serializers.ModelSerializer):
    user_1 = UserSerializer()
    user_2 = UserSerializer()

    class Meta:
        model: Call
        fields: ['duration', 'timestamp', 'videoCall', 'user_1', 'user_2']

class GroupCallSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)

    class Meta:
        model: GroupCall
        fields: ['duration', 'timestamp', 'videoCall', 'participants']