from django import forms
from .models import ChatRoom

class JoinChatRoomForm(forms.Form):
    chat_room = forms.ModelChoiceField(queryset=ChatRoom.objects.all())
    username = forms.CharField(max_length=255)
