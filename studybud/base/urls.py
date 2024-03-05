from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='CreateRoom'),
    path('update-room/<str:pk>/', views.updateRoom, name='UpdateRoom'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='DeleteRoom'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='DeleteMessage'),
    path('profile/<str:pk>/', views.userProfile, name='UserProfile'),
    path('edit-user/', views.updateUser, name='UpdateUser'),
] 