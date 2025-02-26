from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        help_text='' 
    )
    username = forms.CharField(help_text='')
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
