from django.urls import path
from . import views

urlpatterns = [
    path('login', views.users_login),
    path('logout', views.users_logout),
]
