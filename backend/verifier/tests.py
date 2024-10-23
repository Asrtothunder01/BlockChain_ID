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
    
@pytest.fixture
def verify_data():
    return {'status':'pending'}
    
def test_verifier_list_view(api_client):
    url = reverse ('verifier_list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_verifier_create_view(api_client, verifier_data):
    url = reverse ('verifier_list')
    response = api_client.post(url,verifier_data, format = 'json')
    assert response.status_code == statuspp.HTTP_201_CREATED



def test_verify_list_view(api_client):
    url = reverse ('verify_list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_verify_create_view(api_client, verify_data):
    url = reverse ('verify_list')
    response = api_client.post(url,verify_data, format = 'json')
    assert response.status_code == statuspp.HTTP_201_CREATED
