from django.shortcuts import render
from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .serializers import PostSerializer
# Create your views here.

class  PostListView(APIView):
	@extend_schema(
	responses = PostSerializer (many = True)
	
	)
	def get (self, request):
		post = Post.objects.all()
		serializer = PostSerializer (post,many = True)
		return Response (serializer.data)