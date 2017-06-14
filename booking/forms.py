from models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.utils.translation import ugettext_lazy as _


class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        label=_('First Name'),
        max_length=30,
        required=True,
        help_text='Enter your first name',
        widget = forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label=_('Last Name'),
        max_length=30,
        help_text='Enter your last name',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        label=_('Email'),
        max_length=254,
        required=True,
        help_text='Enter you email address',
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Re-enter Password'})
