from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('/', views.index),
    path('register/', views.register, name ='register'),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add-book/', views.add_book, name='add_books'),
    path('del-book/<book_id>', views.delete_book, name='del_books'),
]