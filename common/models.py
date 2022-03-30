from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=20)
    profile = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.nickname