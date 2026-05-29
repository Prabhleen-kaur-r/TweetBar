"""
URL configuration for twitterapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tweet import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Home Page
    path('', views.index, name='index'),

    # Tweet Pages
    path('tweet/', views.tweet_list, name='tweet_list'),
    path('tweet/create/', views.tweet_create, name='tweet_create'),
    path('tweet/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('tweet/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),

    # Like and Dislike
    path('tweet/<int:tweet_id>/like/', views.like_tweet, name='like_tweet'),
    path('tweet/<int:tweet_id>/dislike/', views.dislike_tweet, name='dislike_tweet'),

    # Authentication
    path('register/', views.register, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(
            template_name='registration/logged_out.html'
        ),
        name='logout'
    ),
]

# Media files (images for tweets)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)