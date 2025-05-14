from django import forms
from .models import FamilyPost

class Add_post_form(forms.ModelForm):
    class Meta:
        model = FamilyPost
        fields = ['title', 'content', 'photo', 'video']
        labels = {'title':'Title', 'Content':'Your Content', 'photo':'Photo', 'video':'Video'}
        widgets = {'content':forms.Textarea(attrs={'cols':80})}