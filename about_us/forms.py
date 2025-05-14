from django import forms
from .models import OurHistory

class AddHistory(forms.ModelForm):
    class Meta:
        model = OurHistory
        fields = ['subject', 'content', 'image', 'video']
        labels = {
            'subject':'Name of the Person',
            'content':'History Content',
            'image':'Any related image',
            'video':'Any related video'
            

        }
        widgets = {'content':forms.Textarea(attrs={'col':40, 'rows':10})}