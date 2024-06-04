from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.members, name='members'),
    path('events/', views.events, name='events'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]
