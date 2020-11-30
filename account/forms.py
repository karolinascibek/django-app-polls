from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.hashers import check_password


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


class UserPasswordChangeForm(forms.Form):
    error_message = {
        'new_password1': {
            'required': 'To pole nie moze być puste',
            'min_length': 'hasło powinno zawierać minimum 6 znaków.'
        },
        'new_password2': {
            'required': 'To pole nie moze być puste'
        },
        'old_password': {
            'required': 'To pole nie moze być puste'
        }
    }
    new_password1 = forms.CharField(widget=forms.PasswordInput, min_length=6, error_messages=error_message['new_password1'])
    new_password2 = forms.CharField(required=True, widget=forms.PasswordInput, error_messages=error_message['new_password2'])
    old_password = forms.CharField(required=True, widget=forms.PasswordInput, error_messages=error_message['old_password'] )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not check_password(old_password, self.user.password):
            self.add_error('old_password', "Hasło jest niepoprawne")
        return old_password

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')
        if new_password2 and new_password1 and new_password2 != new_password1:
            print("UserPasswordForm: Podane hasła są rózne")
            self.add_error('new_password2', "Podane hasła są różne")
        print("UserPasswordForm: Podane hasła są poprawne")
        return new_password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
