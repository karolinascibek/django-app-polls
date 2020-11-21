from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms


class UserCreationForm(ModelForm):

    confirm_password = forms.CharField(required=True, min_length=6,
                                       error_messages={
                                           "required": "To pole jest wymagane",
                                           'min_length': "Hasło musi zawierać conajmniej 6 znaków"
                                       })

    class Meta:
        model = get_user_model()
        fields = ['email', 'password','confirm_password','username','is_creator']

        error_messages = {
            'email': {
                'required': 'Wypełnij to pole.',
                'invalid': 'Podany email jest nieporawny',
            },
            'password': {
                'required': "Pole jest wymagane",
            },
            'username': {
                'required': "Pole jest wymagane",
            },
        }

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password2 and password1 and password2 != password1:
            self.add_error('confirm_password',"Hasła muszą być takie same")
        return password2



