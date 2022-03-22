import time

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
import time

# Create your models here.
class Moviews(models.Model):
    datetime = models.DateTimeField(primary_key=True,default=datetime.fromtimestamp(time.time()))
    moviename = models.CharField(max_length=20)
    category = models.CharField(max_length=10)
    moviewline = models.CharField(max_length=50)
    viewdate = models.DateField()
    story = models.TextField()
    moviewimg = models.ImageField(upload_to="moview/", blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 장고 유저 가져오기

    def __str__(self):
        return self.moviename

