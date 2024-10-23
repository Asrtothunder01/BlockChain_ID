from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema

from .models import Document

from .serializer import DocumentSerializer


@extend_schema(
  tags = ['document'],
  
  responses = {200: DocumentSerializer (many = True)},
)

class DocumentListView(ListAPIView):
    
    queryset = Document.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    
    
@extend_schema(
  tags = ['document'],
  
  request = DocumentSerializer(),
  
  responses = {201: DocumentSerializer (many = True)},
)

class DocumentCreateView(ListAPIView):
    
    queryset = Document.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None