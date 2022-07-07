from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('/', views.index),
    path('register/', views.register, name ='register'),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.user_logout, name='logout'),
]