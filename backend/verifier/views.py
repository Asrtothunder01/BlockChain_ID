from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema

from .models import Verifier, Verify

from .serializer import VerifierSerializer, VerifySerializer


@extend_schema(
  tags = ['verify'],
  
  responses = {200: VerifySerializer (many = True)},
)

class VerifyListView(ListAPIView):
    
    queryset = Verify.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    
    
@extend_schema(
  tags = ['verify'],
  
  request = VerifySerializer(),
  
  responses = {201: VerifySerializer (many = True)},
)

class VerifyCreateView(ListAPIView):
    
    queryset = Verify.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    




@extend_schema(
  tags = ['verifier'],
  
  responses = {200: VerifierSerializer (many = True)},
)

class VerifierListView(ListAPIView):
    
    queryset = Verifier.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    
    
@extend_schema(
  tags = ['verifer'],
  
  request = VerifierSerializer(),
  
  responses = {201: VerifierSerializer (many = False)},
)

class VerifierCreateView(ListAPIView):
    
    queryset = Verifier.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    
