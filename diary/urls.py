from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('archive/', views.archive, name='archive'),
    path('archive/<int:post_id>/',views.detail, name = 'detail'),
    path('login/', auth_views.login,
    {'template_name': 'diary/login.html','redirect_authenticated_user': True}, name='login')
]
