from django.urls import path
from . import views

app_name= 'moview'

urlpatterns = [
    path('', views.index, name='index'),    # '/'에 해당되는 path
    path('start/', views.start, name='start'),    # '/'에 해당되는 path
    path('create/', views.add_movie, name='create'),    # '/'에 해당되는 path
    path('<int:movie_id>/', views.movie_detail, name='detail'),
    path('delete/<int:movie_id>/', views.movie_delete, name='delete'),
    path('update/<int:movie_id>/', views.movie_update, name='update'),
    path('choose/', views.movie_choose, name='choose'),
    path('my', views.movie_my, name='mymovie')
]