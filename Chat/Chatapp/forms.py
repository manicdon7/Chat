# chat/forms.py
from django import forms

class SendMessageForm(forms.Form):
    message_text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Type your message here...',
    }))
