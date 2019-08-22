from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('championships/', views.championships, name="championships"),
    path('stadiums/', views.stadiums, name="stadiums"),
]
