import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import Transaction

from .serializers import TransactionSerializer

from rest_framework import status 
# Create your tests here.

@pytest.fixture
def api_client():
    return APIClient()
    
@pytest.fixture
def Transaction_data():
    return {'tx_type':'New Post'}
    
def test_transaction_list_view(api_client):
    url = reverse ('transaction-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_transaction_create_view(api_client, transaction_data):
    url = reverse ('transaction-list')
    response = api_client.post(url, transaction_data, format = 'json')
    assert response.status_code == statuspp.HTTP_201_CREATED
