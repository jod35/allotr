from django.contrib.auth.hashers import make_password

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        user = self.model(
            username=username, email=self.normalize_email(email), **extra_fields
        )

        user.password = make_password(password)

        user.save()

        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(max_length=80, unique=True)
    username = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "date_of_birth"]

    objects = UserManager()

    def __repr__(self) -> str:
        return self.username
