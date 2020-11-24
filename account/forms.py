from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['email']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['username']
        error_messages = {
            'username': {
                'required': 'To Pole nie może być puste.'
            }
        }
