from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(UserManager):
    pass
class User(AbstractUser):
    objects = CustomUserManager()
