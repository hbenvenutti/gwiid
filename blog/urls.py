from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/list/<str:pesquisa>/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment/', views.post_comment, name='post_comment'),
    path('comment/<int:pk>/remove', views.comment_remove, name='comment_remove'),
    path('comment/<int:pk>/approve', views.comment_remove, name='comment_approve'),
    path('championships/', views.championships, name="championships"),
    path('stadiums/', views.stadiums, name="stadiums"),
]
