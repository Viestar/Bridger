from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'username', 'email']
        # fields = '__all__'


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['participants', 'host', 'age', 'country']


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['avatar', 'username', 'first_name', 'email']
