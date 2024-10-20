from django.urls import path

from . import views

urlpatterns = [
  path ('list/',views.DocumentListView.as_view(), name = 'document_list'),
  
  path('create/',views.DocumentCreateView.as_view(), name = 'document_create'),

]