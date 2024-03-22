from django.urls import path
from . import views


app_name = 'accounts_app'

urlpatterns = [
    path('login', views.users_login, name='login'),
    path('logout', views.users_logout, name='logout'),
    path('register', views.users_register, name='register'),
    path('edit', views.user_edit, name='edit'),
]
