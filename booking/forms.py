from models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.utils.translation import ugettext_lazy as _


class SignupForm(UserCreationForm):
    first_name = forms.CharField(label=_('First Name'), max_length=30, required=True, help_text='Enter your first name')
    last_name = forms.CharField(label=_('Last Name'), max_length=30, help_text='Enter your last name')
    email = forms.EmailField(label=_('Email'), max_length=254, required=True, help_text='Enter you email address')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )
