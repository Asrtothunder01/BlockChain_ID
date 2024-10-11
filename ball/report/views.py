from django.shortcuts import render
from  rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from  .models import Report
from .serializers import ReportSerializer
# Create your views here.

class ReportListView(APIView):
	@extend_schema(
	responses = ReportSerializer (many= True)
	)
	
	def get (self, request):
		report = Report.object.all()
		serializer = ReportSerializer (report, many = True)
		return Response (serializer.data)
	