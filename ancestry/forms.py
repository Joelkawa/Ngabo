from django import forms
from .models import Origin

class Edit_Ancestry_Form(forms.ModelForm):
    class Meta:
        model = Origin
        fields = ['origin']
        labels = {'origin':''}
        widgets = {'origin':forms.Textarea(attrs={'col':200, 'rows':10})}

class Add_Ancestry_Form(forms.ModelForm):
    class Meta:
        model = Origin
        fields = ['origin']
        labels = {'origin':''}
        widgets = {'origin':forms.Textarea(attrs={'col':200, 'rows':10})}