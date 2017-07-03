from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
  class Meta:
    model = Feedback
    fields = [
      'name',
      'email',
      'text'
    ]
    widgets = {
    	'name': forms.TextInput(attrs={'placeholder':'Имя','class':'form-control'}),
    	'email': forms.EmailInput(attrs={'placeholder':'Электронная почта','class':'form-control'}),
    	'text': forms.Textarea(attrs={'placeholder':'Сообщение','class':'form-control'}),
    }
    labels = {
    	'name': 'Имя',
    	'email': 'Электронная почта',
    	'text': 'Сообщение'
    }