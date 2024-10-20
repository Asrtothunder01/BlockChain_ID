from rest_restframework.generics import ListAPIView, CreateAPIView

from .models import Verifier, Verify

from .serializer import VerifySerializer,VerifierSerializer

from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema

@extend_schema(
  tags = ['Verify'],
  
  responses = {200: VerifySerializer(many = True)},
)
class VerifyListView(ListAPIView):
    queryset = Verify.objects.all()
    
    serializer_class = VerifySerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None


@extend_schema(
  tags  = ['Verify'],
  
  responses = {201: VerifySerializer (many = False)},
)
class VerifyCreateView(CreateAPIView):
    queryset = Verify.objects.all()
    
    serializer_class = VerifySerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    

@extend_schema(
  tags = ['Verifier'],
  
  responses = {201: VerifierSerializer (many = False)},
)

class VerifierCreateView(CreateAPIView):
    queryset = Verifier.objects.all()
    
    pagination_class = None
    
    permission_classes = [IsAuthenticated]
    
    serializer_class = VerifierSerializer
    
    

class VerifierListView(ListAPIView):
    
    queryset = Verifier.objects.all()
    
    pagination_class = None
    
    permission_classes = [IsAuthenticated]
    
    serializer_class = VerifierSerializer
    
    
    
    
    
    
    
    

