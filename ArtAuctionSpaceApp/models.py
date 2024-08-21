
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models

class Users1Manager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class Users1(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    useremail = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = Users1Manager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['useremail']

    groups = models.ManyToManyField(
        Group,
        related_name='%(class)s_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='%(class)s_set',
        blank=True
    )

    def __str__(self):
        return self.username

    
