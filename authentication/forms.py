from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from django.contrib.auth import authenticate, login, hashers
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
class SignupForm(UserCreationForm):
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
        return self.add_error(
            field = 'username',
            error = 'Must be atleast than 5 letters long'
        )
    def clean_password(self):
        self.clean()
        print(self.cleaned_data)
        print('heelo')
        password = self.cleaned_data.get('password')
        confirm_pass = self.cleaned_data.get('password1')
        if not password == confirm_pass:
            return self.add_error(field = None, error = 'Passwords dont match')
        return self.cleaned_data
    
    # def save(self, commit = True):
    #     user = self.save(commit = False)
    #     user = hashers.make_password(password = user.password)
    #     if commit:
    #         user.save()
    #     return user

# class LoginForm(AuthenticationForm):
#     pass

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length = 254,
        widget = forms.EmailInput(
            attrs = {
                'placeholder' : 'Type your Email',
                'class' : 'form-control'
            }
        ) 
    )
    password = forms.CharField( 
        widget = forms.PasswordInput(
            attrs = {
                'placeholder' : 'please enter password',
                'class' : 'form-control'
            }
        )
    )  
class ForgotPasswordForm(forms.Form):
    old_password = forms.CharField( 
        widget = forms.PasswordInput(
            attrs = {
                'placeholder' : 'please enter old password',
                'class' : 'form-control'
            }
        )
    ) 
    new_password = forms.CharField( 
        widget = forms.PasswordInput(
            attrs = {
                'placeholder' : 'please enter new password',
                'class' : 'form-control'
            }
        )
    )
    confirm_password = forms.CharField( 
        widget = forms.PasswordInput(
            attrs = {
                'placeholder' : 'please confirm password',
                'class' : 'form-control'
            }
        )
    ) 
    def save(self, email):
        if email is None:
            return user
        new_password = forms.cleaned_data.get('new_password')
        confirm_password = forms.cleaned_data.get('confirm_password')
        if not new_password == confirm_password:
            raise forms.ValidationError('Password Mismatch')
        user = User.users.get(email = email)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user


    # def clean(self):
    #     if self.valid():
    #         email = self.cleaned_data.get('email')
    #         password = self.cleaned_data.get('password')
    #         authenticated_user = authenticate(email = email, password = password)
    #         if authenticated_user is None:
    #             return self.errors
    #     return self.cleaned_data

    # def save(self):
    #     if self.is_valid():
            
    #         login()

