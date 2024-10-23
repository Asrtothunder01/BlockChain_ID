from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema

from .models import User

from .serializer import UserSerializer


@extend_schema(
  tags = ['user'],
  
  responses = {200: UserSerializer (many = True)},
)

class UserListView(ListAPIView):
    
    queryset = User.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    
    
@extend_schema(
  tags = ['user'],
  
  request = UserSerializer(),
  
  responses = {201: UserSerializer (many = True)},
)

class UserCreateView(ListAPIView):
    
    queryset = User.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None