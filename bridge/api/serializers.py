from rest_framework.serializers import ModelSerializer
from ..models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
        # fields = '__all__'


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        # fields = '__all__'
        exclude = ['created']
