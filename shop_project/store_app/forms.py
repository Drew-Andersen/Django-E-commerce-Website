from django import forms
from django.contrib.auth.models import User

# Work on editing the form to not show the restraints on the password field until it is clicked
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')