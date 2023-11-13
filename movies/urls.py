from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/comment/create/', views.comments_create, name='comment_create'),
    path('<int:movie_pk>/comment/<int:comment_pk>/delete/', views.comments_delete, name='comment_delete'),
    path('<int:movie_pk>/likes/', views.likes, name='likes'),
    path('map/', views.map_test, name='map_test'),
]