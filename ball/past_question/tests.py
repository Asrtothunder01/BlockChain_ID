import pytest

from django.urls import reverse

from rest_framework import status

from rest_framework.test import APIClient

from .models import QuestionPaper,Subject,Exam

from.serializers import QuestionPaperSerializer, SubjectSerializer, ExamSerializer


@pytest.fixture
def api_client():
	return APIClient()
	

@pytest.fixture
def subject_data():
	return {'name':'New Subject'}
	

@pytest.fixture
def exam_data():
	return {'name':'New Exam'}

@pytest.fixture
def question_paper_data():
	return {'name':'New Question','pdf_file':'test.pdf'}

	
									

# SUBJECT TEST
def test_subject_list_view(api_client):
	url = reverse ('subject-list')
	response = api_client.get(url)
	assert response.status_code == status.HTTP_200_OK
	

def test_subject_create_view(api_client, subject_data):
	url = reverse ('subject-list')
	response = api_client.post(url,subject_data, format = 'json')
	assert response.status_code == status.HTTP_201_CREATED




# EXAM TEST

def test_exam_list_view(api_client):
	url = reverse ('exam-list')
	response = api_client.get(url)
	assert response.status_code == status.HTTP_200_OK
	
def test_exam_create_view(api_client,exam_data):
	url = reverse ('exam-list')
	response = api_client.post(url,exam_data,format = 'json')
	assert response.status_code == status.HTTP_201_CREATED
	
	
# Question Paper Test

def test_question_paper_list_view(api_client):
	url = reverse ('questionpaper-list')
	response = api_client.get(url)
	assert response.status_code == status.HTTP_200_OK

		
def test_question_paper_create_view(api_client, question_paper_data):
	url = reverse ('questionpaper-list')
	response = api_client.post(url, question_paper_data, format = 'multipart')
	assert response.status_code == status.HTTP_201_CREATED
	
	
def test_question_paper_create_view_no_file(api_client, question_paper_data):
	url = reverse ('questionpaper-list')
	response = api_client.post(url,question_paper_data, format ='multipart')
	question_paper_data['pdf_file']='large_file.pdf'
	assert response.status_code == status.HTTP_400_BAD_REQUEST
	

def test_question_paper_create_view_no_file(api_client,question_paper_data):
	url = reverse ('questionpaper-list')
	del question_paper_data['pdf_file']
	response = api_client_post(url, question_paper_data, format = 'json')
	assert response.status_code == status.HTTP_400_BAD_REQUEST
	

	