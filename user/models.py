# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class SwuniManager(BaseUserManager):
    def create_user(self, kakaoId, userName, userImage, password=None, **extra_fields):
        user = self.model(
            kakaoId=kakaoId,
            userName=userName,
            userImage=userImage,
        )
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, kakaoId, userName, userImage, password=None, **extra_fields):
        superuser = self.create_user(
            kakaoId=kakaoId,
            userName=userName,
            userImage=userImage,
            password=password,
        )
        superuser.is_admin = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.is_staff = True
        superuser.save()
        return superuser


class Swuni(AbstractBaseUser, PermissionsMixin):
    kakaoId = models.CharField(max_length=100, unique=True)
    userName = models.CharField(max_length=100)
    userImage = models.ImageField()
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = SwuniManager()

    USERNAME_FIELD = 'kakaoId'
    REQUIRED_FIELDS = ['userName', 'userImage']

    def __str__(self):
        return self.userName