from django.urls import path

from . import views

urlpatterns = [
  path('list/', views.UserListView.as_view(), name = 'User_list'),
  
  path('create/', views.UserCreateView.as_view(),name = 'user_create'),
]