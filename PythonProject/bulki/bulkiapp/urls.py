from django.urls import path
from . import views
from .views import CustomLoginView


urlpatterns = [
    path('bulki/', views.news, name='news'),
    path('bulki/about/', views.about, name='about'),
    path('bulki/links/', views.links, name='links'),
    path('bulki/pool/', views.pool, name='pool'),
    path('bulki/register/', views.register, name='register'),
    path('bulki/article_list/', views.article_list, name='article_list'),
    path('bulki/article_detail/<int:pk>/', views.article_detail, name='article_detail'),
    path('bulki/auth/', CustomLoginView.as_view(), name='auth'),
    path('bulki/add_article/', views.add_article_form, name='add_article'),
    path('bulki/video_page/', views.video_page, name='video_page'),
    path('bulki/profile/', views.profile, name='profile'),
]
