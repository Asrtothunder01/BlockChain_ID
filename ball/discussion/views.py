from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Discussion
from .serializers import DiscussionSerializer
# Create your views here.

class DiscussionListView(APIView):
	@extend_schema(	
	responses = DiscussionSerializer(many = True)
	)
	def get (self, request):
		discuss = Discussion.objects.all ()
		serializer = DiscussionSerializer (discuss,many = True)
		return Response (serializer.data)