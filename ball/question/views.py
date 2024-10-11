from django.shortcuts import render
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.views import APIView
# Create your views here.

class QuestionListView (APIView):
	@extend_schema(
	responses = QuestionSerializer (many = True)
	)
	def get (self, request):
		question = Question.objects.all()
		serializer = QuestionSerializer (question,many= True)
		return Response (serializer.data)