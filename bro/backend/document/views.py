from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.permission import IsAuthenticated

from .models import Document

from drf_spectacular.utils import extend_schema

from .serializers import DocumentSerializer

# DOCUMENT VIEW

@extend_schema(
 tags = ['Document'],
 responses = {200: DocumentSerializer (many = True)},
)

class DocumentListView(ListAPIView):
    queryset = Document.objects.all()
    
    serializer_class = DocumentSerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    
    
    

@extend_schema(
  tags = ['Document'],
  
  request = DocumentSerializer(),
  
  responses = {201: DocumentSerializer ()},
)    

class DocumentCreateView(CreateAPIView):
    
    queryset = Document.objects.all()
    
    serializer_class = DocumentSerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None