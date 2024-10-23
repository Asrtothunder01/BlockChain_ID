import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import Document

from .serializers import DocumentSerializer

from rest_framework import status 
# Create your tests here.

@pytest.fixture
def api_client():
    return APIClient()
    
@pytest.fixture
def document_data():
    return {'document_type':'New Post'}
    
def test_document_list_view(api_client):
    url = reverse ('document-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_document_create_view(api_client,document_data):
    url = reverse ('document-list')
    response = api_client.post(url,document_data, format = 'json')
    assert response.status_code == statuspp.HTTP_201_CREATED
