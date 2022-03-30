from django.contrib import admin

from common.models import CustomUser
from .models import Moviews

admin.site.register(Moviews)
admin.site.register(CustomUser)

# Register your models here.
