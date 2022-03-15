from django.urls import path
from . import views

app_name= 'moview'

urlpatterns = [
    path('', views.index, name='index'),    # '/'에 해당되는 path
    path('moview/create/', views.add_movie, name='create'),    # '/'에 해당되는 path
    path('moview/<int:movie_id>/', views.movie_detail, name='detail'),
    path('moview/delete/<int:movie_id>', views.movie_delete, name='delete'),
    path('moview/update/<int:movie_id>', views.movie_update, name='update'),
    path('moview/choose/', views.movie_choose, name='choose'),
    path('moview/movies/my', views.movie_my, name='mymovie')
]