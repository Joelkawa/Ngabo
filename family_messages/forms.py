from django import forms
from .models import Family_Messages

class Family_Message_Form(forms.ModelForm):
    class Meta:
        model = Family_Messages
        fields = ['text_message','image_message', 'video_message']
        labels = {'text_message':'Write Text', 
                  'image_message':'a photo',
                  'video_message':'a video'
                  }
        wigdets = {
            'text_message':forms.TextInput(),
        }