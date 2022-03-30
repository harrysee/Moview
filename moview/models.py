import time

from django.contrib.auth.models import User, AbstractUser
from django.db import models
from datetime import datetime
import time

# Create your models here.
from config import settings


class Moviews(models.Model):
    moviename = models.CharField(max_length=20)
    category = models.CharField(max_length=10)
    moviewline = models.CharField(max_length=55)
    viewdate = models.DateField()
    story = models.TextField()
    moviewimg = models.ImageField(upload_to="moview/", blank=True,null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 장고 유저 가져오기

    def __str__(self):
        return self.moviewline
