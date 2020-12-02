from django import forms
from .models import Choice


class ChoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['contents', 'question']
