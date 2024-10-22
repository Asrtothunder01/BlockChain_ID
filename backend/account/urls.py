from django.urls import path

from . import views

urlpatterns = [

# User URLS
  path ('list/',views.UserListView.as_view(), name = 'user_list'),

  path('create/',views.UserCreateView.as_view(), name = 'user_create'),
]
