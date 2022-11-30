from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import *
from .models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth import login, logout, mixins
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, HttpResponseForbidden
from django.views import View
from django.views.generic import *

# class ListView(ListView):
#     template_name = 'users.html'
#     queryset = User.users.all()

# class UserProfileView(DetailView):
#     template_name = 'user.html'
#     def get_object(self):
#         user_id = self.kwargs.get('id')
#         return User.users.get(pk = user_id)

# class SignUp(CreateView):
#     template_name = 'signup.html'
#     form_class = SignupForm
    

class Home(View):
    template_name = 'home.html'
    def get(self, request):
        return render(request, self.template_name)

class ListView(mixins.LoginRequiredMixin, View):
    print('is it getting into that')
    template_name = 'users.html'
    object_list = User.users.all()
    login_url = '../../Login'
    context = {
        'object_list' :  object_list 
        }
    def get(self, request):
        print(request.GET.get('next'))
        return render(request, self.template_name, self.context)

class UserProfileView(mixins.LoginRequiredMixin, View):
    login_url = '../../Login'
    template_name = 'user.html'
    def get_object(self, id):
        object = get_object_or_404(User, id = id)
        return object

    def get(self, request, id=None):
        context = {
            'object' : self.get_object(id)
        }
        return render(request, self.template_name, context)

class LoginView(View):
    template_name = 'login.html'
    form = LoginForm()
    context = {
        'form' : form
    }
    def get(self, request):
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email = email, password = password)
            if user:
                login(request, user)
                return redirect('user_profile', id = user.id)
        context = {
            'form' : form
        }
        return render(request, self.template_name, self.context)
            
class Signout(mixins.LoginRequiredMixin, View):
    def post(self, request):
        logout(request)
        return redirect('home')

class ForgotPasswordView(mixins.LoginRequiredMixin, View):
    template_name = 'change_password.html'
    login_url = '../../Login'
    
    def get(self, request):
        form = ForgotPasswordForm()
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            form.save(request.user.email)
            redirect('user_profile')
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)
    



# def signin(request):
    # # form = LoginForm()
    # if request.method == 'POST':
    #     # form = LoginForm(request.POST)
    #     user = authenticate(request, email = request.POST.get('email'), password = request.POST.get('password'))
    #     if user is not None:
    #         print('going going')
    #         login(request , user)
    #         # print()
    #         return redirect('home')
    #         #  form.add_error(field = None, error = forms.ValidationError('Invalid Login'))
    # # context = {
    # #     'form' : form
    # # }
#     return render(request, 'login.html')


# def home(request):
#     return render(request, 'home.html')

def signup(request, *args, **kwargs ):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_view')
    context = {
        'form' : form
    }
    return render(request, 'signup.html', context)


# def signin(request):
#     form = LoginForm()
#     context = {
#         'form' : form
#     }
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request = request, email = email, password = password)
#             if not user:
#                 try:
#                     raise forms.ValidationError('Invalid login')
#                 except forms.ValidationError:
#                     form.add_error(error = 'Invalid Login', field = None)
#                     return render(request, 'login.html', context = {'form' :  form})
#             login(request, user)
#             return redirect('home')
#     return render(request, 'login.html')
        
            
# @login_required
# def signout(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('home')
#     raise Http404
    
# @login_required
# def users_view(request):
#     print(request.user)
#     # try:
#     #     user = User.users.get(username = request.user)
#     #     if not user.is_authenticated:
#     #         return redirect('home')
#     # except User.DoesNotExist:
#     #     messages.error(request, 'Not Registered')
#     #     return redirect('home')
#     # if request.user.is_authenticated
#     session = request.session
#     visits = session.get('visits', 0)
#     visits = visits + 1
#     session['visits'] = visits
#     if (session['visits'] > 15):
#         logout(request)
#         return render(request, 'users.html', context = {
#             'visits' : 'You are a very reliable visitor'
#         })
#     users = User.users.all()
#     context = {
#         'users' : users,
#         'visits' : session['visits']
#     }
#     return render(request, 'users.html', context)

    

        
