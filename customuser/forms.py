from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class SignUpForm(UserCreationForm):
  #  email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email',  'phone', 'name', 'password1', 'password2', )

class UpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'name',  'phone', )

        error_messages = {
             'email': {
                 'unique': "Указанный адрес уже кем-то используется",
             },
            'phone': {
                'unique': "Указанный телефон уже кем-то используется",
            },

        }
