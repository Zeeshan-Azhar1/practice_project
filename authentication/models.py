from django.db.models import *
from django.contrib.auth.models import (AbstractBaseUser, 
    BaseUserManager,
    PermissionsMixin, 
    AbstractUser,
    UserManager,
)

#custom user Manager
# class CustomUserManager(BaseUserManager):

#     def create_user(self, username, email, password):
#         if not email:
#             raise ValueError('Email must be specified')
#         email = self.normalize_email(email)
#         user = self.model(
#             email = email,
#             username = username,
#         )
#         user.set_password(password)
#         user.save(using = self._db)
#         return user
    
#     def create_superuser(self, username, email, password):
#         user = self.create_user(username, email, password)
#         user.is_superuser = True
#         user.is_admin = True
#         user.is_staff = True
#         user.save(using = self._db )
#         return user

# custom user model
class User(AbstractUser):
    email = EmailField(
        max_length = 254,
        verbose_name = 'email',
        unique = True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['username']
    users = UserManager()
    
    def __str__(self):
        return self.username
    # username = CharField(
    #     max_length = 20,
    #     verbose_name = 'username',
    #     unique = True,
    # )
    # gender = CharField(
    #     choices = [
    #         ('M', 'Male'),
    #         ('F', 'Female'),
    #         ('O', 'Other'),
    #     ],
    #     max_length = 3, 
    #     null = True,
    #     blank = True, 
    # )
    # is_active = BooleanField(
    #     default = True,
    # )
    # is_admin = BooleanField(
    #     default = False,
    # )
    # is_staff = BooleanField(
    #     default = False,
    # )
    # is_superuser = BooleanField(
    #     default = False,
    # )
    
