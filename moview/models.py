from django.db import models

# Create your models here.
class Moviews(models.Model):
    moviewname = models.CharField(max_length=20)
    category = models.IntegerField(null=False)
    moviewline = models.CharField(max_length=50)
    calender = models.DateTimeField()
    diary = models.TextField()
    moviewimg = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.moviewname

