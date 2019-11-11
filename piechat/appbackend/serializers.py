from rest_framework import serializers
from .models import Account, Chats
from django.contrib.auth import get_user_model

UserModel = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'email')


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = ('sender', 'message', 'receiver', 'sent')