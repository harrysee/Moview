from django.urls import path
from . import views

app_name= 'moview'

urlpatterns = [
    path('', views.index, name='index'),    # '/'에 해당되는 path
    path('add/', views.addmovie, name='add'),    # '/'에 해당되는 path
]