from django.urls import path
from translations import views


app_name = 'translations'


urlpatterns = [
    path('', views.home, name='home'),
    
]

