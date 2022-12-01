from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_routes),
    path('rooms/', views.get_rooms),
    path('messages/', views.get_messages),
    path('users/', views.get_users),
    path('users/<str:pk>/', views.get_user),
]
