from django.urls import path
from . import views
from home_app.views import partial_view



app_name = 'home_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('sidebar', partial_view, name='sidebar'),
    
]
