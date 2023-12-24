from django.urls import path
from app.auth import login, register, logout
from app.reel import reel_watch, reels, upload


urlpatterns = [
    path('auth/login/',login.login,name='login'),
    path('auth/register/',register.register,name='register'),
    path('auth/logout/',logout.logout,name='logout'),

    path('',reels.home_reels,name='home'),
    path('reel/<str:reeluuid>/',reel_watch.reel,name='reel'),
    path('upload/',upload.upload_reel,name='upload'),
]