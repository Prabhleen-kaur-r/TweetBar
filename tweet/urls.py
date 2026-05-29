from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('tweets/', views.tweet_list, name='tweet_list'),

    path('create/', views.tweet_create, name='tweet_create'),

    path('edit/<int:tweet_id>/', views.tweet_edit, name='tweet_edit'),

    path('delete/<int:tweet_id>/', views.tweet_delete, name='tweet_delete'),

    path('like/<int:tweet_id>/', views.like_tweet, name='like_tweet'),

    path('dislike/<int:tweet_id>/', views.dislike_tweet, name='dislike_tweet'),

    path('register/', views.register, name='register'),

]