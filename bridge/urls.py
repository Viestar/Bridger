from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.register_user, name="register"),
    path('logout/', views.logoutuser, name="logout"),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('update-message/<str:pk>/', views.update_message, name="update-message"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.delete_message, name="delete-message"),
    path('message/<str:pk>/', views.message, name="message"),
    path('user-profile/<str:pk>/', views.user_profile, name="user-profile"),
    path('update-profile/', views.update_profile, name="update-profile"),
    path('topics/', views.topics, name="topics"),
    path('activities/', views.activities, name="activities"),
]
