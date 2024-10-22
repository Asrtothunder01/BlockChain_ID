from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema

from .models import Transaction

from .serializer import TransactionSerializer


@extend_schema(
  tags = ['Transaction'],
  
  responses = {200: TransactionSerializer (many = True)},
)

class TransactionListView(ListAPIView):
    
    queryset = Transaction.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    
    
@extend_schema(
  tags = ['Transaction'],
  
  request = TransactionSerializer(),
  
  responses = {201: TransactionSerializer (many = True)},
)

class TransactionCreateView(ListAPIView):
    
    queryset = Transaction.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None