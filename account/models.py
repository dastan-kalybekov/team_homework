from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    telegram_chat_id = models.CharField(max_length=9)
    password = models.CharField(max_length=20)


