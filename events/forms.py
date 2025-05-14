from django import forms
from .models import FamilyEvents


class AddEventForm(forms.ModelForm):
    class Meta:
        model = FamilyEvents
        fields = [
            'name',
            'content',
            'image',
            'video',
            'happening_date',
        ]
        labels = {
            'name':'Name of the Event',
            'content':'Event Details',
            'image':'Upload any related Photos',
            'video':'Upload any related Videos',
            'happening_date':'Happening Date',
                  }
        
        widgets = {'content':forms.Textarea(attrs={'cols':80})}