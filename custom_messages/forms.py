from django import forms
from .models import Message

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'recipient',
            'contents',
            'reply_to',
        ]
        labels = {
            'recipient':'To:', 
            'contents':'Message:', 
            'reply_to':'Reply',
        }
        widgets = {'reply_to':forms.HiddenInput(),}

    def __init__(self, *args, **kwargs):
        reply_to = kwargs.pop('reply_to',None)
        super().__init__(*args, **kwargs)
        if reply_to:
            self.fields['recipient'].widget=forms.HiddenInput()
            self.fields['recipient'].initial = reply_to.sender
        else:
            self.fields['reply_to'].widget = forms.HiddenInput()


