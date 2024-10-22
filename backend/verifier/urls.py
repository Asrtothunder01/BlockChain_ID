from django.urls import path

from . import views

urlpatterns = [

# VERIFIER URLS
  path ('list/',views.VerfierListView.as_view(), name = 'verifier_list'),

  path('create/',views.VerifierCreateView.as_view(), name = 'verifier_create'),

# Verify URLS 

    path('list/', views.VerifyListView.as_view(), name = 'verify_list'),
  
  path ('create/', views.VerifyCreateView.as_view(), name = 'verify_create'),

]