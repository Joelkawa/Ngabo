from django import forms
from .models import Media

class Upload_Media_Form(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['heading', 'images', 'video']
        labels = {'heading':'Title',
                  'images':'Photo',
                  'video':'Video'
                  }
        widgets = {
            'heading': forms.TextInput(attrs={'placeholder': 'Subject'}),
        }
        
        