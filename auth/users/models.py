from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
from .validators import generate_random_code

# Добавляю свои кастомные поля


class User(AbstractUser):
    phone_number = models.CharField("phone", max_length=50, blank=True)
    passcode = models.PositiveIntegerField("passcode")
    invite_code = models.CharField(
        "referal code", max_length=6, default=generate_random_code(6), unique=True)
    activated_invite_code = models.CharField(
        "activated invite code", max_length=6, blank=True)
