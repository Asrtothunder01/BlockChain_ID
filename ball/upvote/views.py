from django.shortcuts import render
from  rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from  .models import Upvote
from .serializers import UpvoteSerializer
# Create your views here.

class UpvoteListView(APIView):
	@extend_schema(
	responses = UpvoteSerializer (many= True)
	)
	
	def get (self, request):
		upvote = Upvote.object.all()
		serializer = UpvoteSerializer (upvote, many = True)
		return Response (serializer.data)
