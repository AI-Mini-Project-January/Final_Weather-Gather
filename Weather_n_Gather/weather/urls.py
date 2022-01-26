from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('get_weather/', views.get_weather),
]