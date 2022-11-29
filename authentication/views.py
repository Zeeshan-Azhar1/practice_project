from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import User

def home(request):
    return render(request, 'home.html')

def signup(request, *args, **kwargs ):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form.error_messages)
        if form.is_valid():
            form.save()
            return redirect('users_view')
    context = {
        'form' : form
    }
    return render(request, 'signup.html', context)

def users_view(request):
    users = User.users.all()
    context = {
        'users' : users
    }
    return render(request, 'users.html', context)

    

        
