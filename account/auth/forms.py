from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms


class UserCreationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=6,
                               error_messages={
                                   "required": "To pole jest wymagane",
                                   'min_length': "Hasło musi zawierać conajmniej 6 znaków"
                               })
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput,
                                       error_messages={"required": "To pole jest wymagane"})

    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'is_creator']

        error_messages = {
            'email': {
                'required': 'To pole nie może być puste.',
                'invalid': 'Podany email jest niepoprawny.',
            },
            'password': {
                'required': 'To pole nie może być puste.',
            },
            'username': {
                'required': 'To pole nie może być puste.',
            },
        }

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password2 and password1 and password2 != password1:
            self.add_error('confirm_password', "Hasła muszą być takie same")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    error_messages = {
        'email': {
            'required': 'To pole nie może być puste.',
            'invalid': 'Podany email jest niepoprawny',
        },
        'password': {
            'required': "To pole nie może być puste.",
        },
    }
    email = forms.EmailField(required=True, error_messages=error_messages['email'])
    password = forms.CharField(required=True, error_messages=error_messages['password'])


