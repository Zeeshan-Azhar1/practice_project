"""custom_authentication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Signup/', signup, name = 'signup'),
    path('home/', Home.as_view(), name = 'home'),
    path('Users/', ListView.as_view(), name = 'users_view' ),
    path('User/<int:id>/', UserProfileView.as_view(), name = 'user_profile'),
    path('Login/', LoginView.as_view(), name = 'login'),
    path('Logout/', Signout.as_view(), name = 'logout'),
    path('Forget_Password/', ForgotPasswordView.as_view(), name = 'forget_password'),
]
