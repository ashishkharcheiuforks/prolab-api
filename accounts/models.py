from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

class ProUser(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(_('full name'), max_length=50, blank=True)
    username = models.CharField(max_length=20, null=False, unique=True)
    email     = models.EmailField(verbose_name='email address', max_length=255, unique=True)

    # password field supplied by AbstractBaseUser
    # last_login field supplied by AbstractBaseUser
    # is_superuser field provided by PermissionsMixin
    # groups field provided by PermissionsMixin
    # user_permissions field provided by PermissionsMixin

    # activation_key = models.CharField(max_length=255, default=1)
    # email_validated = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'username',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_name(self):
        return self.name
