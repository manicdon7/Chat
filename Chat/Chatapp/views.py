from django.views.generic import TemplateView
from django.shortcuts import render
from .form import JoinChatRoomForm
class ChatRoomView(TemplateView):
    template_name = 'chat/main.html'

    def get(self, request, *args, **kwargs):
        form = JoinChatRoomForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = JoinChatRoomForm(request.POST)
        if form.is_valid():
            chat_room = form.cleaned_data['chat_room']
            username = form.cleaned_data['username']
            return render(request, self.template_name, {'chat_room': chat_room, 'username': username, 'form': form})
        else:
            return render(request, self.template_name, {'form': form})
