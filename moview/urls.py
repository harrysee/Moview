from django.urls import path
from . import views

app_name= 'moview'

urlpatterns = [
    path('', views.index, name='index'),    # '/'에 해당되는 path
    path('moview/create/', views.add_movie, name='create'),    # '/'에 해당되는 path
    path('moview/<int:movie_id>/', views.movie_detail, name='detail')
]