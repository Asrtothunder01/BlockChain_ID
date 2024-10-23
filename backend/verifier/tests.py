import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import Verifier, Verify

from .serializers import VerifierSerializer, VerifySerializer

from rest_framework import status 
# Create your tests here.

@pytest.fixture
def api_client():
    return APIClient()
    
@pytest.fixture
def verifier_data():
    return {'name':'New Post'}
    
def test_verifier_list_view(api_client):
    url = reverse ('verifier-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_verifier_create_view(api_client, verifier_data):
    url = reverse ('verifier-list')
    response = api_client.post(url,verifier_data, format = 'json')
    assert response.status_code == statuspp.HTTP_201_CREATED
