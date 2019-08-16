from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('championships/', views.championships, name="championships"),
    path('stadiums/', views.stadiums, name="stadiums"),
]
