import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import User

from .serializers import UserSerializer

from rest_framework import status 
# Create your tests here.

@pytest.fixture
def api_client():
    return APIClient()
    
@pytest.fixture
def user_data():
    return {'name':'New Post'}
    
def test_user_list_view(api_client):
    url = reverse ('user-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_user_create_view(api_client,user_data):
    url = reverse ('user-list')
    response = api_client.post(url,user_data, format = 'json')
    assert response.status_code == statuspp.HTTP_201_CREATED
