from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
class SignupForm(UserCreationForm):
    email = forms.EmailField()    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not (len(username) < 5 ):
            return username
        raise forms.ValidationError('Length Must be greater than 4')
    def clean_password(self):
        password = self.password1
        confirm_password = self.password2
        if not password == confirm_password:
            raise forms.ValidationError('Passwords Mismatch error')
        return password

    
